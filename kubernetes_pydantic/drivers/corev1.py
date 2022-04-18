from typing import Callable

from kubernetes_pydantic.drivers.apicore import K8sApiCore


class NamespaceApiCore(K8sApiCore):
    for_cluster = True

    @property
    def creator(self) -> Callable:
        return self.api.corev1.create_namespace

    @property
    def merger(self) -> Callable:
        return self.api.corev1.patch_namespace

    @property
    def replacer(self) -> Callable:
        return self.api.corev1.replace_namespace

    @property
    def deleter(self) -> Callable:
        return self.api.corev1.delete_namespace

    @property
    def lister(self) -> Callable:
        return self.api.corev1.list_namespace

    @property
    def getter(self) -> Callable:
        return self.api.corev1.read_namespace


class NodeApiCore(K8sApiCore):
    for_cluster = True

    @property
    def creator(self) -> Callable:
        return self.api.corev1.create_node

    @property
    def merger(self) -> Callable:
        return self.api.corev1.patch_node

    @property
    def replacer(self) -> Callable:
        return self.api.corev1.replace_node

    @property
    def deleter(self) -> Callable:
        return self.api.corev1.delete_node

    @property
    def lister(self) -> Callable:
        return self.api.corev1.list_node

    @property
    def getter(self) -> Callable:
        return self.api.corev1.read_node


class PersistentVolumeApiCore(K8sApiCore):
    for_cluster = True

    @property
    def creator(self) -> Callable:
        return self.api.corev1.create_persistent_volume

    @property
    def merger(self) -> Callable:
        return self.api.corev1.patch_persistent_volume

    @property
    def replacer(self) -> Callable:
        return self.api.corev1.replace_persistent_volume

    @property
    def deleter(self) -> Callable:
        return self.api.corev1.delete_persistent_volume

    @property
    def lister(self) -> Callable:
        return self.api.corev1.list_persistent_volume

    @property
    def getter(self) -> Callable:
        return self.api.corev1.read_persistent_volume


class ConfigMapApiCore(K8sApiCore):
    @property
    def creator(self) -> Callable:
        return self.api.corev1.create_namespaced_config_map

    @property
    def merger(self) -> Callable:
        return self.api.corev1.patch_namespaced_config_map

    @property
    def replacer(self) -> Callable:
        return self.api.corev1.replace_namespaced_config_map

    @property
    def deleter(self) -> Callable:
        return self.api.corev1.delete_namespaced_config_map

    @property
    def lister(self) -> Callable:
        return self.api.corev1.list_namespaced_config_map

    @property
    def getter(self) -> Callable:
        return self.api.corev1.read_namespaced_config_map


class EndpointsApiCore(K8sApiCore):
    @property
    def creator(self) -> Callable:
        return self.api.corev1.create_namespaced_endpoints

    @property
    def merger(self) -> Callable:
        return self.api.corev1.patch_namespaced_endpoints

    @property
    def replacer(self) -> Callable:
        return self.api.corev1.replace_namespaced_endpoints

    @property
    def deleter(self) -> Callable:
        return self.api.corev1.delete_namespaced_endpoints

    @property
    def lister(self) -> Callable:
        return self.api.corev1.list_namespaced_endpoints

    @property
    def getter(self) -> Callable:
        return self.api.corev1.read_namespaced_endpoints


class EventApiCore(K8sApiCore):
    @property
    def creator(self) -> Callable:
        return self.api.corev1.create_namespaced_event

    @property
    def merger(self) -> Callable:
        return self.api.corev1.patch_namespaced_event

    @property
    def replacer(self) -> Callable:
        return self.api.corev1.replace_namespaced_event

    @property
    def deleter(self) -> Callable:
        return self.api.corev1.delete_namespaced_event

    @property
    def lister(self) -> Callable:
        return self.api.corev1.list_namespaced_event

    @property
    def getter(self) -> Callable:
        return self.api.corev1.read_namespaced_event


class LimitRangeApiCore(K8sApiCore):
    @property
    def creator(self) -> Callable:
        return self.api.corev1.create_namespaced_limit_range

    @property
    def merger(self) -> Callable:
        return self.api.corev1.patch_namespaced_limit_range

    @property
    def replacer(self) -> Callable:
        return self.api.corev1.replace_namespaced_limit_range

    @property
    def deleter(self) -> Callable:
        return self.api.corev1.delete_namespaced_limit_range

    @property
    def lister(self) -> Callable:
        return self.api.corev1.list_namespaced_limit_range

    @property
    def getter(self) -> Callable:
        return self.api.corev1.read_namespaced_limit_range


class PersistentVolumeClaimApiCore(K8sApiCore):
    @property
    def creator(self) -> Callable:
        return self.api.corev1.create_namespaced_persistent_volume_claim

    @property
    def merger(self) -> Callable:
        return self.api.corev1.patch_namespaced_persistent_volume_claim

    @property
    def replacer(self) -> Callable:
        return self.api.corev1.replace_namespaced_persistent_volume_claim

    @property
    def deleter(self) -> Callable:
        return self.api.corev1.delete_namespaced_persistent_volume_claim

    @property
    def lister(self) -> Callable:
        return self.api.corev1.list_namespaced_persistent_volume_claim

    @property
    def getter(self) -> Callable:
        return self.api.corev1.read_namespaced_persistent_volume_claim


class PodApiCore(K8sApiCore):
    @property
    def creator(self) -> Callable:
        return self.api.corev1.create_namespaced_pod

    @property
    def merger(self) -> Callable:
        return self.api.corev1.patch_namespaced_pod

    @property
    def replacer(self) -> Callable:
        return self.api.corev1.replace_namespaced_pod

    @property
    def deleter(self) -> Callable:
        return self.api.corev1.delete_namespaced_pod

    @property
    def lister(self) -> Callable:
        return self.api.corev1.list_namespaced_pod

    @property
    def getter(self) -> Callable:
        return self.api.corev1.read_namespaced_pod


class PodTemplateApiCore(K8sApiCore):
    @property
    def creator(self) -> Callable:
        return self.api.corev1.create_namespaced_pod_template

    @property
    def merger(self) -> Callable:
        return self.api.corev1.patch_namespaced_pod_template

    @property
    def replacer(self) -> Callable:
        return self.api.corev1.replace_namespaced_pod_template

    @property
    def deleter(self) -> Callable:
        return self.api.corev1.delete_namespaced_pod_template

    @property
    def lister(self) -> Callable:
        return self.api.corev1.list_namespaced_pod_template

    @property
    def getter(self) -> Callable:
        return self.api.corev1.read_namespaced_pod_template


class ResourceQuotaApiCore(K8sApiCore):
    @property
    def creator(self) -> Callable:
        return self.api.corev1.create_namespaced_resource_quota

    @property
    def merger(self) -> Callable:
        return self.api.corev1.patch_namespaced_resource_quota

    @property
    def replacer(self) -> Callable:
        return self.api.corev1.replace_namespaced_resource_quota

    @property
    def deleter(self) -> Callable:
        return self.api.corev1.delete_namespaced_resource_quota

    @property
    def lister(self) -> Callable:
        return self.api.corev1.list_namespaced_resource_quota

    @property
    def getter(self) -> Callable:
        return self.api.corev1.read_namespaced_resource_quota


class SecretApiCore(K8sApiCore):
    @property
    def creator(self) -> Callable:
        return self.api.corev1.create_namespaced_secret

    @property
    def merger(self) -> Callable:
        return self.api.corev1.patch_namespaced_secret

    @property
    def replacer(self) -> Callable:
        return self.api.corev1.replace_namespaced_secret

    @property
    def deleter(self) -> Callable:
        return self.api.corev1.delete_namespaced_secret

    @property
    def lister(self) -> Callable:
        return self.api.corev1.list_namespaced_secret

    @property
    def getter(self) -> Callable:
        return self.api.corev1.read_namespaced_secret


class ServiceAccountApiCore(K8sApiCore):
    @property
    def creator(self) -> Callable:
        return self.api.corev1.create_namespaced_service_account

    @property
    def merger(self) -> Callable:
        return self.api.corev1.patch_namespaced_service_account

    @property
    def replacer(self) -> Callable:
        return self.api.corev1.replace_namespaced_service_account

    @property
    def deleter(self) -> Callable:
        return self.api.corev1.delete_namespaced_service_account

    @property
    def lister(self) -> Callable:
        return self.api.corev1.list_namespaced_service_account

    @property
    def getter(self) -> Callable:
        return self.api.corev1.read_namespaced_service_account


class ServiceApiCore(K8sApiCore):
    @property
    def creator(self) -> Callable:
        return self.api.corev1.create_namespaced_service

    @property
    def merger(self) -> Callable:
        return self.api.corev1.patch_namespaced_service

    @property
    def replacer(self) -> Callable:
        return self.api.corev1.replace_namespaced_service

    @property
    def deleter(self) -> Callable:
        return self.api.corev1.delete_namespaced_service

    @property
    def lister(self) -> Callable:
        return self.api.corev1.list_namespaced_service

    @property
    def getter(self) -> Callable:
        return self.api.corev1.read_namespaced_service
