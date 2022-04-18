from kubernetes_pydantic.drivers.pipelinev1beta1 import (
    TaskApiCore,
    PipelineRunApiCore,
    PipelineApiCore,
    TaskRunApiCore,
    ClusterTaskApiCore,
)
from kubernetes_pydantic.types import pipelinev1beta1
from kubernetes_pydantic.drivers.apiwrapper import K8sWrapApi


class PipelineApi(K8sWrapApi[pipelinev1beta1.Pipeline]):
    model = pipelinev1beta1.Pipeline

    @classmethod
    def new(cls, namespace: str, **kwargs) -> "PipelineApi":
        return PipelineApi(core=PipelineApiCore(namespace=namespace, **kwargs))


class PipelineRunApi(K8sWrapApi[pipelinev1beta1.PipelineRun]):
    model = pipelinev1beta1.PipelineRun

    @classmethod
    def new(cls, namespace: str, **kwargs) -> "PipelineRunApi":
        return PipelineRunApi(core=PipelineRunApiCore(namespace=namespace, **kwargs))


class TaskApi(K8sWrapApi[pipelinev1beta1.Task]):
    model = pipelinev1beta1.Task

    @classmethod
    def new(cls, namespace: str, **kwargs) -> "TaskApi":
        return TaskApi(core=TaskApiCore(namespace=namespace, **kwargs))


class TaskRunApi(K8sWrapApi[pipelinev1beta1.TaskRun]):
    model = pipelinev1beta1.TaskRun

    @classmethod
    def new(cls, namespace: str, **kwargs) -> "TaskRunApi":
        return TaskRunApi(core=TaskRunApiCore(namespace=namespace, **kwargs))


class ClusterTaskApi(K8sWrapApi[pipelinev1beta1.ClusterTask]):
    model = pipelinev1beta1.ClusterTask

    @classmethod
    def new(cls, **kwargs) -> "ClusterTaskApi":
        return ClusterTaskApi(core=ClusterTaskApiCore(**kwargs))
