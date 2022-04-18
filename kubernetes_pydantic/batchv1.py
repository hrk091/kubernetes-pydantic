from kubernetes_pydantic.drivers.appsv1 import (
    DaemonSetApiCore,
    DeploymentApiCore,
    ReplicaSetApiCore,
    StatefulSetApiCore,
)
from kubernetes_pydantic.drivers.batchv1 import CronJobApiCore, JobApiCore
from kubernetes_pydantic.types import batchv1
from kubernetes_pydantic.drivers.apiwrapper import K8sWrapApi


class CronJobApi(K8sWrapApi[batchv1.CronJob]):
    model = batchv1.CronJob

    @classmethod
    def new(cls, namespace: str, **kwargs) -> "CronJobApi":
        return CronJobApi(core=CronJobApiCore(namespace=namespace, **kwargs))


class JobApi(K8sWrapApi[batchv1.Job]):
    model = batchv1.Job

    @classmethod
    def new(cls, namespace: str, **kwargs) -> "JobApi":
        return JobApi(core=JobApiCore(namespace=namespace, **kwargs))
