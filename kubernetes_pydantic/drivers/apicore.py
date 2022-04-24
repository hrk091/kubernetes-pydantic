from typing import NamedTuple, ClassVar, Optional, Union, Callable

from kubernetes import client as K8sClient
from kubernetes.client import Configuration

from kubernetes_pydantic.drivers.utils import k8s_config


class ApiClient(K8sClient.ApiClient):
    # NOTE This is hack to use apply-patch+yaml content-type which needed for k8s server side apply,
    #      but it is unable to use since original kubernetes-client does not support this content-type yet.
    #      https://github.com/kubernetes-client/python/pull/959

    def select_header_content_type(self, content_types):
        """Returns `Content-Type` based on an array of content_types provided.

        :param content_types: List of content-generated.
        :return: Content-Type (e.g. application/json).
        """
        if not content_types:
            return "application/json"

        content_types = [x.lower() for x in content_types]

        # --- custom start ---
        # INFO change content-type to use k8s server side apply
        if "application/apply-patch+yaml" in content_types:
            return "application/apply-patch+yaml"
        # --- custom end ---
        if "application/json" in content_types or "*/*" in content_types:
            return "application/json"
        else:
            return content_types[0]


class K8sOriginalApi:
    config: Configuration
    client: K8sClient.ApiClient
    appsv1: K8sClient.AppsV1Api
    corev1: K8sClient.CoreV1Api
    rbacv1: K8sClient.RbacAuthorizationV1Api
    batchv1: K8sClient.BatchV1Api
    networkingv1: K8sClient.NetworkingV1Api
    custom: K8sClient.CustomObjectsApi

    def __init__(self, config: Optional[Configuration] = None, client: Optional[ApiClient] = None):
        self.config = config if config else k8s_config()
        self.client = client if client else K8sClient.ApiClient(self.config)
        # self.client = client if client else ApiClient(config)
        self.appsv1 = K8sClient.AppsV1Api(self.client)
        self.corev1 = K8sClient.CoreV1Api(self.client)
        self.rbacv1 = K8sClient.RbacAuthorizationV1Api(self.client)
        self.batchv1 = K8sClient.BatchV1Api(self.client)
        self.networkingv1 = K8sClient.NetworkingV1Api(self.client)
        self.custom = K8sClient.CustomObjectsApi(self.client)


class Empty(NamedTuple):
    pass


class Namespace(NamedTuple):
    namespace: str


class GVK(NamedTuple):
    group: str
    version: str
    kind: str


class GVNK(NamedTuple):
    group: str
    version: str
    namespace: str
    kind: str


class K8sApiCore:
    for_cluster: ClassVar[bool] = False
    api: K8sOriginalApi
    namespace: Optional[str]

    def __init__(
        self,
        namespace: Optional[str] = None,
        config: Optional[Configuration] = None,
        client: Optional[ApiClient] = None,
    ):
        if self.for_cluster and namespace:
            raise AssertionError("cannot set namespace to ClusterApi")
        if not self.for_cluster and not namespace:
            raise AssertionError("namespace needed for NamespacedApi")
        self.api = K8sOriginalApi(config, client)
        self.namespace = namespace

    @property
    def gvnk(self) -> Union[Empty, Namespace, GVK, GVNK]:
        if self.for_cluster:
            return Empty()

        if not self.namespace:
            raise ValueError("Namespace is required for non-cluster resource.")
        return Namespace(self.namespace)

    def namespaced_name(self, name: str) -> list:
        return [name, *self.gvnk]

    @property
    def creator(self) -> Callable:
        raise NotImplementedError

    @property
    def merger(self) -> Callable:
        raise NotImplementedError

    @property
    def replacer(self) -> Callable:
        raise NotImplementedError

    @property
    def deleter(self) -> Callable:
        raise NotImplementedError

    @property
    def getter(self) -> Callable:
        raise NotImplementedError

    @property
    def lister(self) -> Callable:
        raise NotImplementedError

    def close(self):
        self.api.client.close()


class K8SCustomApiCore(K8sApiCore):
    group: ClassVar[str]
    version: ClassVar[str]
    kind: ClassVar[str]  # lowercase plural

    @property
    def gvnk(self) -> Union[Empty, Namespace, GVK, GVNK]:
        if self.for_cluster:
            return GVK(self.group, self.version, self.kind)

        if not self.namespace:
            raise ValueError("Namespace is required for non-cluster resource.")
        return GVNK(self.group, self.version, self.namespace, self.kind)

    def namespaced_name(self, name: str) -> list:
        return [*self.gvnk, name]

    @property
    def creator(self) -> Callable:
        if self.for_cluster:
            return self.api.custom.create_cluster_custom_object
        else:
            return self.api.custom.create_namespaced_custom_object

    @property
    def merger(self) -> Callable:
        if self.for_cluster:
            return self.api.custom.patch_cluster_custom_object
        else:
            return self.api.custom.patch_namespaced_custom_object

    @property
    def replacer(self) -> Callable:
        if self.for_cluster:
            return self.api.custom.replace_cluster_custom_object
        else:
            return self.api.custom.replace_namespaced_custom_object

    @property
    def deleter(self) -> Callable:
        if self.for_cluster:
            return self.api.custom.delete_cluster_custom_object
        else:
            return self.api.custom.delete_namespaced_custom_object

    @property
    def lister(self) -> Callable:
        if self.for_cluster:
            return self.api.custom.list_cluster_custom_object
        else:
            return self.api.custom.list_namespaced_custom_object

    @property
    def getter(self) -> Callable:
        if self.for_cluster:
            return self.api.custom.get_cluster_custom_object
        else:
            return self.api.custom.get_namespaced_custom_object
