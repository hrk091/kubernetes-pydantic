from kubernetes_pydantic.drivers.networkingv1 import IngressApiCore, IngressClassApiCore
from kubernetes_pydantic.types import networkingv1
from kubernetes_pydantic.drivers.apiwrapper import K8sWrapApi


class IngressApi(K8sWrapApi[networkingv1.Ingress]):
    model = networkingv1.Ingress

    @classmethod
    def new(cls, namespace: str, **kwargs) -> "IngressApi":
        return IngressApi(core=IngressApiCore(namespace=namespace, **kwargs))


class IngressClassApi(K8sWrapApi[networkingv1.IngressClass]):
    model = networkingv1.IngressClass

    @classmethod
    def new(cls, **kwargs) -> "IngressClassApi":
        return IngressClassApi(core=IngressClassApiCore(**kwargs))
