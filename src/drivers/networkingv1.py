from typing import Callable

from src.drivers.apicore import K8sApiCore


class IngressClassApiCore(K8sApiCore):
    for_cluster = True

    @property
    def creator(self) -> Callable:
        return self.api.networkingv1.create_ingress_class

    @property
    def merger(self) -> Callable:
        return self.api.networkingv1.patch_ingress_class

    @property
    def replacer(self) -> Callable:
        return self.api.networkingv1.replace_ingress_class

    @property
    def deleter(self) -> Callable:
        return self.api.networkingv1.delete_ingress_class

    @property
    def lister(self) -> Callable:
        return self.api.networkingv1.list_ingress_class

    @property
    def getter(self) -> Callable:
        return self.api.networkingv1.read_ingress_class


class IngressApiCore(K8sApiCore):
    @property
    def creator(self) -> Callable:
        return self.api.networkingv1.create_namespaced_ingress

    @property
    def merger(self) -> Callable:
        return self.api.networkingv1.patch_namespaced_ingress

    @property
    def replacer(self) -> Callable:
        return self.api.networkingv1.replace_namespaced_ingress

    @property
    def deleter(self) -> Callable:
        return self.api.networkingv1.delete_namespaced_ingress

    @property
    def lister(self) -> Callable:
        return self.api.networkingv1.list_namespaced_ingress

    @property
    def getter(self) -> Callable:
        return self.api.networkingv1.read_namespaced_ingress
