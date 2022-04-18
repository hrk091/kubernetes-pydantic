from typing import Optional, Protocol

from kubernetes.client import ApiException

from src.drivers.apiwrapper import T
from src.generated.github.com.tektoncd.pipeline.pkg.apis.pipeline import v1beta1 as _pipelinev1beta1
from src.generated.io.k8s.api.apps import v1 as _appsv1
from src.generated.io.k8s.api.core import v1 as _corev1
from src.generated.io.k8s.api.rbac import v1 as _rbacv1
from src.generated.io.k8s.api.batch import v1 as _batchv1
from src.generated.io.k8s.api.networking import v1 as _networkingv1
from src.generated.io.k8s.apimachinery.pkg.apis.meta import v1 as _metav1

appsv1 = _appsv1
corev1 = _corev1
metav1 = _metav1
rbacv1 = _rbacv1
batchv1 = _batchv1
networkingv1 = _networkingv1
pipelinev1beta1 = _pipelinev1beta1


class K8sApiInterface(Protocol[T]):
    async def create_or_replace(self, name: str, body: T, **kwargs) -> tuple[Optional[T], Optional[ApiException]]:
        ...

    async def create(self, body: T, **kwargs) -> tuple[Optional[T], Optional[ApiException]]:
        ...

    async def merge(self, name: str, body: T, **kwargs) -> tuple[Optional[T], Optional[ApiException]]:
        ...

    async def replace(self, name: str, body: T, **kwargs) -> tuple[Optional[T], Optional[ApiException]]:
        ...

    async def delete(self, name: str, **kwargs) -> Optional[ApiException]:
        ...

    async def get(self, name: str, **kwargs) -> tuple[Optional[T], Optional[ApiException]]:
        ...

    async def list(self, **kwargs) -> tuple[list[T], Optional[ApiException]]:
        ...
