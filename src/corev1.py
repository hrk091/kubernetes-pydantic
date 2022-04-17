from src.drivers.corev1 import NamespaceApiCore, SecretApiCore, PvcAPiCore, SAApiCore, EventsApiCore
from src.types import corev1
from src.drivers.apiwrapper import K8sWrapApi


class NamespaceApi(K8sWrapApi[corev1.Namespace]):
    model = corev1.Namespace

    @classmethod
    def new(cls, **kwargs) -> "NamespaceApi":
        return NamespaceApi(core=NamespaceApiCore(**kwargs))


class SecretApi(K8sWrapApi[corev1.Secret]):
    model = corev1.Secret

    @classmethod
    def new(cls, namespace: str, **kwargs) -> "SecretApi":
        return SecretApi(core=SecretApiCore(namespace=namespace, **kwargs))


class PvcApi(K8sWrapApi[corev1.PersistentVolumeClaim]):
    model = corev1.PersistentVolumeClaim

    @classmethod
    def new(cls, namespace: str, **kwargs) -> "PvcApi":
        return PvcApi(core=PvcAPiCore(namespace=namespace, **kwargs))


class SAApi(K8sWrapApi[corev1.ServiceAccount]):
    model = corev1.ServiceAccount

    @classmethod
    def new(cls, namespace: str, **kwargs) -> "SAApi":
        return SAApi(core=SAApiCore(namespace=namespace, **kwargs))


class EventsApi(K8sWrapApi[corev1.Event]):
    model = corev1.Event

    @classmethod
    def new(cls, namespace: str, **kwargs) -> "EventsApi":
        return EventsApi(core=EventsApiCore(namespace=namespace, **kwargs))
