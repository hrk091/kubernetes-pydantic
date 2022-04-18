from src.drivers.rbacv1 import RoleApiCore, RoleBindingApiCore, ClusterRoleApiCore, ClusterRoleBindingApiCore
from src.types import rbacv1
from src.drivers.apiwrapper import K8sWrapApi


class ClusterRoleApi(K8sWrapApi[rbacv1.ClusterRole]):
    model = rbacv1.ClusterRole

    @classmethod
    def new(cls, **kwargs) -> "ClusterRoleApi":
        return ClusterRoleApi(core=ClusterRoleApiCore(**kwargs))


class ClusterRoleBindingApi(K8sWrapApi[rbacv1.ClusterRoleBinding]):
    model = rbacv1.ClusterRoleBinding

    @classmethod
    def new(cls, **kwargs) -> "ClusterRoleBindingApi":
        return ClusterRoleBindingApi(core=ClusterRoleBindingApiCore(**kwargs))


class RoleApi(K8sWrapApi[rbacv1.Role]):
    model = rbacv1.Role

    @classmethod
    def new(cls, namespace: str, **kwargs) -> "RoleApi":
        return RoleApi(core=RoleApiCore(namespace=namespace, **kwargs))


class RoleBindingApi(K8sWrapApi[rbacv1.RoleBinding]):
    model = rbacv1.RoleBinding

    @classmethod
    def new(cls, namespace: str, **kwargs) -> "RoleBindingApi":
        return RoleBindingApi(core=RoleBindingApiCore(namespace=namespace, **kwargs))
