from typing import Callable

from src.drivers.apicore import K8sApiCore


class ClusterRoleApiCore(K8sApiCore):
    for_cluster = True

    @property
    def creator(self) -> Callable:
        return self.api.rbacv1.create_cluster_role

    @property
    def merger(self) -> Callable:
        return self.api.rbacv1.patch_cluster_role

    @property
    def replacer(self) -> Callable:
        return self.api.rbacv1.replace_cluster_role

    @property
    def deleter(self) -> Callable:
        return self.api.rbacv1.delete_cluster_role

    @property
    def lister(self) -> Callable:
        return self.api.rbacv1.list_cluster_role

    @property
    def getter(self) -> Callable:
        return self.api.rbacv1.read_cluster_role


class ClusterRoleBindingApiCore(K8sApiCore):
    for_cluster = True

    @property
    def creator(self) -> Callable:
        return self.api.rbacv1.create_cluster_role_binding

    @property
    def merger(self) -> Callable:
        return self.api.rbacv1.patch_cluster_role_binding

    @property
    def replacer(self) -> Callable:
        return self.api.rbacv1.replace_cluster_role_binding

    @property
    def deleter(self) -> Callable:
        return self.api.rbacv1.delete_cluster_role_binding

    @property
    def lister(self) -> Callable:
        return self.api.rbacv1.list_cluster_role_binding

    @property
    def getter(self) -> Callable:
        return self.api.rbacv1.read_cluster_role_binding


class RoleApiCore(K8sApiCore):
    @property
    def creator(self) -> Callable:
        return self.api.rbacv1.create_namespaced_role

    @property
    def merger(self) -> Callable:
        return self.api.rbacv1.patch_namespaced_role

    @property
    def replacer(self) -> Callable:
        return self.api.rbacv1.replace_namespaced_role

    @property
    def deleter(self) -> Callable:
        return self.api.rbacv1.delete_namespaced_role

    @property
    def lister(self) -> Callable:
        return self.api.rbacv1.list_namespaced_role

    @property
    def getter(self) -> Callable:
        return self.api.rbacv1.read_namespaced_role


class RoleBindingApiCore(K8sApiCore):
    @property
    def creator(self) -> Callable:
        return self.api.rbacv1.create_namespaced_role_binding

    @property
    def merger(self) -> Callable:
        return self.api.rbacv1.patch_namespaced_role_binding

    @property
    def replacer(self) -> Callable:
        return self.api.rbacv1.replace_namespaced_role_binding

    @property
    def deleter(self) -> Callable:
        return self.api.rbacv1.delete_namespaced_role_binding

    @property
    def lister(self) -> Callable:
        return self.api.rbacv1.list_namespaced_role_binding

    @property
    def getter(self) -> Callable:
        return self.api.rbacv1.read_namespaced_role_binding
