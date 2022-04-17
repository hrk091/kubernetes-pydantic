from unittest.mock import MagicMock

import pytest
from kubernetes.client import Configuration, ApiClient
from pydantic_factories import ModelFactory

from src.types import pipelinev1beta1
from src.pipelinev1beta1 import ClusterTaskApi
from src.conftest import DUMMY_NAMESPACE, asyncresult_return_value


@pytest.fixture
def cluster_task(meta) -> pipelinev1beta1.ClusterTask:
    class Factory(ModelFactory):
        __model__ = pipelinev1beta1.ClusterTask
        api_version = "tekton.dev/v1beta1"
        kind = "ClusterTask"
        metadata = meta

    return Factory.build()


@pytest.mark.asyncio
async def test_custom_object_create(cluster_task):
    api = ClusterTaskApi.new(config=MagicMock(Configuration), client=MagicMock(ApiClient))

    ret_val = asyncresult_return_value(cluster_task.dict())
    api.core.api.custom.create_cluster_custom_object = MagicMock(return_value=ret_val)

    res = await api.create(cluster_task)
    api.core.api.custom.create_cluster_custom_object.assert_called_once_with(
        "tekton.dev", "v1beta1", "clustertasks", cluster_task.dict(by_alias=True), async_req=True
    )
    assert res == (cluster_task, None)


@pytest.mark.asyncio
async def test_custom_object_merge(cluster_task):
    api = ClusterTaskApi.new(config=MagicMock(Configuration), client=MagicMock(ApiClient))

    ret_val = asyncresult_return_value(cluster_task.dict())
    api.core.api.custom.patch_cluster_custom_object = MagicMock(return_value=ret_val)

    res = await api.merge(cluster_task.metadata.name, cluster_task)
    api.core.api.custom.patch_cluster_custom_object.assert_called_once_with(
        "tekton.dev",
        "v1beta1",
        "clustertasks",
        cluster_task.metadata.name,
        cluster_task.dict(by_alias=True),
        async_req=True,
    )
    assert res == (cluster_task, None)


@pytest.mark.asyncio
async def test_custom_object_replace(cluster_task):
    api = ClusterTaskApi.new(config=MagicMock(Configuration), client=MagicMock(ApiClient))

    ret_val = asyncresult_return_value(cluster_task.dict())
    api.core.api.custom.replace_cluster_custom_object = MagicMock(return_value=ret_val)

    res = await api.replace(cluster_task.metadata.name, cluster_task)
    api.core.api.custom.replace_cluster_custom_object.assert_called_once_with(
        "tekton.dev",
        "v1beta1",
        "clustertasks",
        cluster_task.metadata.name,
        cluster_task.dict(by_alias=True),
        async_req=True,
    )
    assert res == (cluster_task, None)


@pytest.mark.asyncio
async def test_custom_object_delete(cluster_task):
    api = ClusterTaskApi.new(config=MagicMock(Configuration), client=MagicMock(ApiClient))

    ret_val = asyncresult_return_value(cluster_task.dict())
    api.core.api.custom.delete_cluster_custom_object = MagicMock(return_value=ret_val)

    res = await api.delete(cluster_task.metadata.name)
    api.core.api.custom.delete_cluster_custom_object.assert_called_once_with(
        "tekton.dev", "v1beta1", "clustertasks", cluster_task.metadata.name, async_req=True
    )
    assert res is None


@pytest.mark.asyncio
async def test_custom_object_get(cluster_task):
    api = ClusterTaskApi.new(config=MagicMock(Configuration), client=MagicMock(ApiClient))

    ret_val = asyncresult_return_value(cluster_task.dict())
    api.core.api.custom.get_cluster_custom_object = MagicMock(return_value=ret_val)

    res = await api.get(cluster_task.metadata.name)
    api.core.api.custom.get_cluster_custom_object.assert_called_once_with(
        "tekton.dev", "v1beta1", "clustertasks", cluster_task.metadata.name, async_req=True
    )
    assert res == (cluster_task, None)


@pytest.mark.asyncio
async def test_custom_object_list(cluster_task):
    api = ClusterTaskApi.new(config=MagicMock(Configuration), client=MagicMock(ApiClient))

    ret_val = asyncresult_return_value({"items": [cluster_task.dict()]})
    api.core.api.custom.list_cluster_custom_object = MagicMock(return_value=ret_val)

    res = await api.list()
    api.core.api.custom.list_cluster_custom_object.assert_called_once_with(
        "tekton.dev", "v1beta1", "clustertasks", async_req=True
    )
    assert res == ([cluster_task], None)
