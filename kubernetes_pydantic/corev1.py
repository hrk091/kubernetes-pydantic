from kubernetes_pydantic.drivers.corev1 import (
    NamespaceApiCore,
    SecretApiCore,
    PersistentVolumeClaimApiCore,
    ServiceAccountApiCore,
    NodeApiCore,
    PersistentVolumeApiCore,
    ConfigMapApiCore,
    EndpointsApiCore,
    EventApiCore,
    LimitRangeApiCore,
    PodApiCore,
    PodTemplateApiCore,
    ResourceQuotaApiCore,
    ServiceApiCore,
)
from kubernetes_pydantic.types import corev1
from kubernetes_pydantic.drivers.apiwrapper import K8sWrapApi


class NamespaceApi(K8sWrapApi[corev1.Namespace]):
    model = corev1.Namespace

    @classmethod
    def new(cls, **kwargs) -> "NamespaceApi":
        return NamespaceApi(core=NamespaceApiCore(**kwargs))


class NodeApi(K8sWrapApi[corev1.Node]):
    model = corev1.Node

    @classmethod
    def new(cls, **kwargs) -> "NodeApi":
        return NodeApi(core=NodeApiCore(**kwargs))


class PersistentVolumeApi(K8sWrapApi[corev1.PersistentVolume]):
    model = corev1.PersistentVolume

    @classmethod
    def new(cls, **kwargs) -> "PersistentVolumeApi":
        return PersistentVolumeApi(core=PersistentVolumeApiCore(**kwargs))


class ConfigMapApi(K8sWrapApi[corev1.ConfigMap]):
    model = corev1.ConfigMap

    @classmethod
    def new(cls, namespace: str, **kwargs) -> "ConfigMapApi":
        return ConfigMapApi(core=ConfigMapApiCore(namespace=namespace, **kwargs))


class EndpointsApi(K8sWrapApi[corev1.Endpoints]):
    model = corev1.Endpoints

    @classmethod
    def new(cls, namespace: str, **kwargs) -> "EndpointsApi":
        return EndpointsApi(core=EndpointsApiCore(namespace=namespace, **kwargs))


class EventApi(K8sWrapApi[corev1.Event]):
    model = corev1.Event

    @classmethod
    def new(cls, namespace: str, **kwargs) -> "EventApi":
        return EventApi(core=EventApiCore(namespace=namespace, **kwargs))


class LimitRangeApi(K8sWrapApi[corev1.LimitRange]):
    model = corev1.LimitRange

    @classmethod
    def new(cls, namespace: str, **kwargs) -> "LimitRangeApi":
        return LimitRangeApi(core=LimitRangeApiCore(namespace=namespace, **kwargs))


class PersistentVolumeClaimApi(K8sWrapApi[corev1.PersistentVolumeClaim]):
    model = corev1.PersistentVolumeClaim

    @classmethod
    def new(cls, namespace: str, **kwargs) -> "PersistentVolumeClaimApi":
        return PersistentVolumeClaimApi(core=PersistentVolumeClaimApiCore(namespace=namespace, **kwargs))


class PodApi(K8sWrapApi[corev1.Pod]):
    model = corev1.Pod

    @classmethod
    def new(cls, namespace: str, **kwargs) -> "PodApi":
        return PodApi(core=PodApiCore(namespace=namespace, **kwargs))


class PodTemplateApi(K8sWrapApi[corev1.PodTemplate]):
    model = corev1.PodTemplate

    @classmethod
    def new(cls, namespace: str, **kwargs) -> "PodTemplateApi":
        return PodTemplateApi(core=PodTemplateApiCore(namespace=namespace, **kwargs))


class ResourceQuotaApi(K8sWrapApi[corev1.ResourceQuota]):
    model = corev1.ResourceQuota

    @classmethod
    def new(cls, namespace: str, **kwargs) -> "ResourceQuotaApi":
        return ResourceQuotaApi(core=ResourceQuotaApiCore(namespace=namespace, **kwargs))


class SecretApi(K8sWrapApi[corev1.Secret]):
    model = corev1.Secret

    @classmethod
    def new(cls, namespace: str, **kwargs) -> "SecretApi":
        return SecretApi(core=SecretApiCore(namespace=namespace, **kwargs))


class ServiceAccountApi(K8sWrapApi[corev1.ServiceAccount]):
    model = corev1.ServiceAccount

    @classmethod
    def new(cls, namespace: str, **kwargs) -> "ServiceAccountApi":
        return ServiceAccountApi(core=ServiceAccountApiCore(namespace=namespace, **kwargs))


class ServiceApi(K8sWrapApi[corev1.Service]):
    model = corev1.Service

    @classmethod
    def new(cls, namespace: str, **kwargs) -> "ServiceApi":
        return ServiceApi(core=ServiceApiCore(namespace=namespace, **kwargs))
