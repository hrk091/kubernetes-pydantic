from unittest.mock import MagicMock

import pytest
from kubernetes.client import Configuration, ApiClient, V1Namespace, V1NamespaceList
from pydantic_factories import ModelFactory

from kubernetes_pydantic.types import corev1
from kubernetes_pydantic.corev1 import NamespaceApi
from kubernetes_pydantic.conftest import DUMMY_NAMESPACE, asyncresult_return_value


@pytest.fixture
def namespace(meta) -> corev1.Namespace:
    class Factory(ModelFactory):
        __model__ = corev1.Namespace
        api_version = "v1"
        kind = "Namespace"
        metadata = meta

    return Factory.build()


@pytest.mark.asyncio
async def test_namespace_create(namespace):
    api = NamespaceApi.new(config=MagicMock(Configuration), client=MagicMock(ApiClient))

    ret_val = asyncresult_return_value(V1Namespace(**namespace.dict()))
    api.core.api.corev1.create_namespace = MagicMock(return_value=ret_val)

    res = await api.create(namespace)
    api.core.api.corev1.create_namespace.assert_called_once_with(namespace.dict(by_alias=True), async_req=True)
    assert res == (namespace, None)


@pytest.mark.asyncio
async def test_namespace_merge(namespace):
    api = NamespaceApi.new(config=MagicMock(Configuration), client=MagicMock(ApiClient))

    ret_val = asyncresult_return_value(V1Namespace(**namespace.dict()))
    api.core.api.corev1.patch_namespace = MagicMock(return_value=ret_val)

    res = await api.merge(namespace.metadata.name, namespace)
    api.core.api.corev1.patch_namespace.assert_called_once_with(
        namespace.metadata.name, namespace.dict(by_alias=True), async_req=True
    )
    assert res == (namespace, None)


@pytest.mark.asyncio
async def test_namespace_replace(namespace):
    api = NamespaceApi.new(config=MagicMock(Configuration), client=MagicMock(ApiClient))

    ret_val = asyncresult_return_value(V1Namespace(**namespace.dict()))
    api.core.api.corev1.replace_namespace = MagicMock(return_value=ret_val)

    res = await api.replace(namespace.metadata.name, namespace)
    api.core.api.corev1.replace_namespace.assert_called_once_with(
        namespace.metadata.name, namespace.dict(by_alias=True), async_req=True
    )
    assert res == (namespace, None)


@pytest.mark.asyncio
async def test_namespace_delete(namespace):
    api = NamespaceApi.new(config=MagicMock(Configuration), client=MagicMock(ApiClient))

    ret_val = asyncresult_return_value(V1Namespace(**namespace.dict()))
    api.core.api.corev1.delete_namespace = MagicMock(return_value=ret_val)

    res = await api.delete(namespace.metadata.name)
    api.core.api.corev1.delete_namespace.assert_called_once_with(namespace.metadata.name, async_req=True)
    assert res is None


@pytest.mark.asyncio
async def test_namespace_get(namespace):
    api = NamespaceApi.new(config=MagicMock(Configuration), client=MagicMock(ApiClient))

    ret_val = asyncresult_return_value(V1Namespace(**namespace.dict()))
    api.core.api.corev1.read_namespace = MagicMock(return_value=ret_val)

    res = await api.get(namespace.metadata.name)
    api.core.api.corev1.read_namespace.assert_called_once_with(namespace.metadata.name, async_req=True)
    assert res == (namespace, None)


@pytest.mark.asyncio
async def test_namespace_list(namespace):
    api = NamespaceApi.new(config=MagicMock(Configuration), client=MagicMock(ApiClient))

    ret_val = asyncresult_return_value(V1NamespaceList(items=[namespace.dict()]))
    api.core.api.corev1.list_namespace = MagicMock(return_value=ret_val)

    res = await api.list()
    api.core.api.corev1.list_namespace.assert_called_once_with(async_req=True)
    assert res == ([namespace], None)
