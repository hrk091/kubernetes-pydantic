from typing import Callable

from src.drivers.apicore import K8sApiCore


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


class PvcAPiCore(K8sApiCore):
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


class SAApiCore(K8sApiCore):
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


class EventsApiCore(K8sApiCore):
    @property
    def lister(self) -> Callable:
        return self.api.corev1.list_namespaced_event
