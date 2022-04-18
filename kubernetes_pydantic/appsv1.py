from kubernetes_pydantic.drivers.appsv1 import (
    DaemonSetApiCore,
    DeploymentApiCore,
    ReplicaSetApiCore,
    StatefulSetApiCore,
)
from kubernetes_pydantic.types import appsv1
from kubernetes_pydantic.drivers.apiwrapper import K8sWrapApi


class DaemonSetApi(K8sWrapApi[appsv1.DaemonSet]):
    model = appsv1.DaemonSet

    @classmethod
    def new(cls, namespace: str, **kwargs) -> "DaemonSetApi":
        return DaemonSetApi(core=DaemonSetApiCore(namespace=namespace, **kwargs))


class DeploymentApi(K8sWrapApi[appsv1.Deployment]):
    model = appsv1.Deployment

    @classmethod
    def new(cls, namespace: str, **kwargs) -> "DeploymentApi":
        return DeploymentApi(core=DeploymentApiCore(namespace=namespace, **kwargs))


class ReplicaSetApi(K8sWrapApi[appsv1.ReplicaSet]):
    model = appsv1.ReplicaSet

    @classmethod
    def new(cls, namespace: str, **kwargs) -> "ReplicaSetApi":
        return ReplicaSetApi(core=ReplicaSetApiCore(namespace=namespace, **kwargs))


class StatefulSetApi(K8sWrapApi[appsv1.StatefulSet]):
    model = appsv1.StatefulSet

    @classmethod
    def new(cls, namespace: str, **kwargs) -> "StatefulSetApi":
        return StatefulSetApi(core=StatefulSetApiCore(namespace=namespace, **kwargs))
