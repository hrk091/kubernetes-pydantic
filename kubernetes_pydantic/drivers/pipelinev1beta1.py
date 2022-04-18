from kubernetes_pydantic.types import pipelinev1beta1

from kubernetes_pydantic.drivers.apicore import K8SCustomApiCore


class PipelineApiCore(K8SCustomApiCore):
    group = "tekton.dev"
    version = "v1beta1"
    kind = "pipelines"


class PipelineRunApiCore(K8SCustomApiCore):
    group = "tekton.dev"
    version = "v1beta1"
    kind = "pipelineruns"


class TaskApiCore(K8SCustomApiCore):
    group = "tekton.dev"
    version = "v1beta1"
    kind = "tasks"


class TaskRunApiCore(K8SCustomApiCore):
    model = pipelinev1beta1.TaskRun
    group = "tekton.dev"
    version = "v1beta1"
    kind = "taskruns"


class ClusterTaskApiCore(K8SCustomApiCore):
    for_cluster = True
    model = pipelinev1beta1.ClusterTask
    group = "tekton.dev"
    version = "v1beta1"
    kind = "clustertasks"
