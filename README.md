# kubernetes-pydantic
Wrapper of [kubernetes-client/python](https://github.com/kubernetes-client/python) for better typing leveraging Pydantic.


## Installation

From source:

```
git clone https://github.com/hrk091/kubernetes-pydantic
pip install kubernetes-pydantic
```

## Examples

List all pods:

```python
import asyncio

from kubernetes_pydantic.corev1 import PodApi

async def main():
    api = PodApi.new(namespace="kube-system")

    items, err = await api.list()
    if err:
        raise err
    for i in items:
        print(i.metadata.name)


if __name__ == "__main__":
    asyncio.run(main())
```

You can see type hints of all nested fields on your IDE since all of them are Pydantic types.


## Capabilities

Following resources are supported:

apps/v1
- DaemonSet
- Deployment
- ReplicaSet
- StatefulSet

batch/v1
- CronJob
- Job

core/v1
- ConfigMap
- Endpoints
- Event
- LimitRange
- Namespace
- Node
- PersistentVolume
- PersistentVolumeClaim
- Pod
- PodTemplate
- ResourceQuota
- SecretApi
- ServiceAccount
- Service

networking.k8s.io/v1
- IngressClass
- Ingress

rbac.authorization.k8s.io/v1
- ClusterRoleBinding
- ClusterRole
- RoleBinding
- Role

tekton.dev/v1beta1
- ClusterTask
- PipelineRun
- Pipeline
- TaskRun
- Task


## Caveats

- Watch API is not supported yet. 
