from typing import Callable

from kubernetes_pydantic.drivers.apicore import K8sApiCore


class DaemonSetApiCore(K8sApiCore):
    @property
    def creator(self) -> Callable:
        return self.api.appsv1.create_namespaced_daemon_set

    @property
    def merger(self) -> Callable:
        return self.api.appsv1.patch_namespaced_daemon_set

    @property
    def replacer(self) -> Callable:
        return self.api.appsv1.replace_namespaced_daemon_set

    @property
    def deleter(self) -> Callable:
        return self.api.appsv1.delete_namespaced_daemon_set

    @property
    def lister(self) -> Callable:
        return self.api.appsv1.list_namespaced_daemon_set

    @property
    def getter(self) -> Callable:
        return self.api.appsv1.read_namespaced_daemon_set


class DeploymentApiCore(K8sApiCore):
    @property
    def creator(self) -> Callable:
        return self.api.appsv1.create_namespaced_deployment

    @property
    def merger(self) -> Callable:
        return self.api.appsv1.patch_namespaced_deployment

    @property
    def replacer(self) -> Callable:
        return self.api.appsv1.replace_namespaced_deployment

    @property
    def deleter(self) -> Callable:
        return self.api.appsv1.delete_namespaced_deployment

    @property
    def lister(self) -> Callable:
        return self.api.appsv1.list_namespaced_deployment

    @property
    def getter(self) -> Callable:
        return self.api.appsv1.read_namespaced_deployment


class ReplicaSetApiCore(K8sApiCore):
    @property
    def creator(self) -> Callable:
        return self.api.appsv1.create_namespaced_replica_set

    @property
    def merger(self) -> Callable:
        return self.api.appsv1.patch_namespaced_replica_set

    @property
    def replacer(self) -> Callable:
        return self.api.appsv1.replace_namespaced_replica_set

    @property
    def deleter(self) -> Callable:
        return self.api.appsv1.delete_namespaced_replica_set

    @property
    def lister(self) -> Callable:
        return self.api.appsv1.list_namespaced_replica_set

    @property
    def getter(self) -> Callable:
        return self.api.appsv1.read_namespaced_replica_set


class StatefulSetApiCore(K8sApiCore):
    @property
    def creator(self) -> Callable:
        return self.api.appsv1.create_namespaced_stateful_set

    @property
    def merger(self) -> Callable:
        return self.api.appsv1.patch_namespaced_stateful_set

    @property
    def replacer(self) -> Callable:
        return self.api.appsv1.replace_namespaced_stateful_set

    @property
    def deleter(self) -> Callable:
        return self.api.appsv1.delete_namespaced_stateful_set

    @property
    def lister(self) -> Callable:
        return self.api.appsv1.list_namespaced_stateful_set

    @property
    def getter(self) -> Callable:
        return self.api.appsv1.read_namespaced_stateful_set
