from src.drivers.appsv1 import DaemonSetApiCore, DeploymentApiCore, ReplicaSetApiCore, StatefulSetApiCore
from src.drivers.batchv1 import CronJobApiCore, JobApiCore
from src.types import batchv1
from src.drivers.apiwrapper import K8sWrapApi


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
