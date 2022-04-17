from unittest.mock import MagicMock

import pytest
from kubernetes.client import Configuration, ApiClient
from pydantic_factories import ModelFactory

from src.types import pipelinev1beta1
from src.pipelinev1beta1 import TaskApi
from src.conftest import DUMMY_NAMESPACE, asyncresult_return_value


@pytest.fixture
def task(meta) -> pipelinev1beta1.Task:
    class Factory(ModelFactory):
        __model__ = pipelinev1beta1.Task
        api_version = "tekton.dev/v1beta1"
        kind = "Task"
        metadata = meta

    return Factory.build()


@pytest.mark.asyncio
async def test_custom_object_create(task):
    api = TaskApi.new(namespace=DUMMY_NAMESPACE, config=MagicMock(Configuration), client=MagicMock(ApiClient))

    ret_val = asyncresult_return_value(task.dict())
    api.core.api.custom.create_namespaced_custom_object = MagicMock(return_value=ret_val)

    res = await api.create(task)
    api.core.api.custom.create_namespaced_custom_object.assert_called_once_with(
        "tekton.dev", "v1beta1", DUMMY_NAMESPACE, "tasks", task.dict(by_alias=True), async_req=True
    )
    assert res == (task, None)


@pytest.mark.asyncio
async def test_custom_object_merge(task):
    api = TaskApi.new(namespace=DUMMY_NAMESPACE, config=MagicMock(Configuration), client=MagicMock(ApiClient))

    ret_val = asyncresult_return_value(task.dict())
    api.core.api.custom.patch_namespaced_custom_object = MagicMock(return_value=ret_val)

    res = await api.merge(task.metadata.name, task)
    api.core.api.custom.patch_namespaced_custom_object.assert_called_once_with(
        "tekton.dev", "v1beta1", DUMMY_NAMESPACE, "tasks", task.metadata.name, task.dict(by_alias=True), async_req=True
    )
    assert res == (task, None)


@pytest.mark.asyncio
async def test_custom_object_replace(task):
    api = TaskApi.new(namespace=DUMMY_NAMESPACE, config=MagicMock(Configuration), client=MagicMock(ApiClient))

    ret_val = asyncresult_return_value(task.dict())
    api.core.api.custom.replace_namespaced_custom_object = MagicMock(return_value=ret_val)

    res = await api.replace(task.metadata.name, task)
    api.core.api.custom.replace_namespaced_custom_object.assert_called_once_with(
        "tekton.dev", "v1beta1", DUMMY_NAMESPACE, "tasks", task.metadata.name, task.dict(by_alias=True), async_req=True
    )
    assert res == (task, None)


@pytest.mark.asyncio
async def test_custom_object_delete(task):
    api = TaskApi.new(namespace=DUMMY_NAMESPACE, config=MagicMock(Configuration), client=MagicMock(ApiClient))

    ret_val = asyncresult_return_value(task.dict())
    api.core.api.custom.delete_namespaced_custom_object = MagicMock(return_value=ret_val)

    res = await api.delete(task.metadata.name)
    api.core.api.custom.delete_namespaced_custom_object.assert_called_once_with(
        "tekton.dev", "v1beta1", DUMMY_NAMESPACE, "tasks", task.metadata.name, async_req=True
    )
    assert res is None


@pytest.mark.asyncio
async def test_custom_object_get(task):
    api = TaskApi.new(namespace=DUMMY_NAMESPACE, config=MagicMock(Configuration), client=MagicMock(ApiClient))

    ret_val = asyncresult_return_value(task.dict())
    api.core.api.custom.get_namespaced_custom_object = MagicMock(return_value=ret_val)

    res = await api.get(task.metadata.name)
    api.core.api.custom.get_namespaced_custom_object.assert_called_once_with(
        "tekton.dev", "v1beta1", DUMMY_NAMESPACE, "tasks", task.metadata.name, async_req=True
    )
    assert res == (task, None)


@pytest.mark.asyncio
async def test_custom_object_list(task):
    api = TaskApi.new(namespace=DUMMY_NAMESPACE, config=MagicMock(Configuration), client=MagicMock(ApiClient))

    ret_val = asyncresult_return_value({"items": [task.dict()]})
    api.core.api.custom.list_namespaced_custom_object = MagicMock(return_value=ret_val)

    res = await api.list()
    api.core.api.custom.list_namespaced_custom_object.assert_called_once_with(
        "tekton.dev", "v1beta1", DUMMY_NAMESPACE, "tasks", async_req=True
    )
    assert res == ([task], None)
