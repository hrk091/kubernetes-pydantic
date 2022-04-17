from unittest.mock import MagicMock

import pytest
from kubernetes.client import Configuration, ApiClient, V1Role, V1RoleList
from pydantic_factories import ModelFactory

from src.types import rbacv1
from src.rbacv1 import RoleApi
from src.conftest import DUMMY_NAMESPACE, asyncresult_return_value


@pytest.fixture
def role(meta) -> rbacv1.Role:
    class Factory(ModelFactory):
        __model__ = rbacv1.Role
        api_version = "rbac.authorization.k8s.io/v1"
        kind = "Role"
        metadata = meta

    return Factory.build()


@pytest.mark.asyncio
async def test_role_create(role):
    api = RoleApi.new(namespace=DUMMY_NAMESPACE, config=MagicMock(Configuration), client=MagicMock(ApiClient))

    ret_val = asyncresult_return_value(V1Role(**role.dict()))
    api.core.api.rbacv1.create_namespaced_role = MagicMock(return_value=ret_val)

    res = await api.create(role)
    api.core.api.rbacv1.create_namespaced_role.assert_called_once_with(
        role.metadata.namespace, role.dict(by_alias=True), async_req=True
    )
    assert res == (role, None)


@pytest.mark.asyncio
async def test_role_merge(role):
    api = RoleApi.new(namespace=DUMMY_NAMESPACE, config=MagicMock(Configuration), client=MagicMock(ApiClient))

    ret_val = asyncresult_return_value(V1Role(**role.dict()))
    api.core.api.rbacv1.patch_namespaced_role = MagicMock(return_value=ret_val)

    res = await api.merge(role.metadata.name, role)
    api.core.api.rbacv1.patch_namespaced_role.assert_called_once_with(
        role.metadata.name, role.metadata.namespace, role.dict(by_alias=True), async_req=True
    )
    assert res == (role, None)


@pytest.mark.asyncio
async def test_role_replace(role):
    api = RoleApi.new(namespace=DUMMY_NAMESPACE, config=MagicMock(Configuration), client=MagicMock(ApiClient))

    ret_val = asyncresult_return_value(V1Role(**role.dict()))
    api.core.api.rbacv1.replace_namespaced_role = MagicMock(return_value=ret_val)

    res = await api.replace(role.metadata.name, role)
    api.core.api.rbacv1.replace_namespaced_role.assert_called_once_with(
        role.metadata.name, role.metadata.namespace, role.dict(by_alias=True), async_req=True
    )
    assert res == (role, None)


@pytest.mark.asyncio
async def test_role_delete(role):
    api = RoleApi.new(namespace=DUMMY_NAMESPACE, config=MagicMock(Configuration), client=MagicMock(ApiClient))

    ret_val = asyncresult_return_value(V1Role(**role.dict()))
    api.core.api.rbacv1.delete_namespaced_role = MagicMock(return_value=ret_val)

    res = await api.delete(role.metadata.name)
    api.core.api.rbacv1.delete_namespaced_role.assert_called_once_with(
        role.metadata.name, role.metadata.namespace, async_req=True
    )
    assert res is None


@pytest.mark.asyncio
async def test_role_get(role):
    api = RoleApi.new(namespace=DUMMY_NAMESPACE, config=MagicMock(Configuration), client=MagicMock(ApiClient))

    ret_val = asyncresult_return_value(V1Role(**role.dict()))
    api.core.api.rbacv1.read_namespaced_role = MagicMock(return_value=ret_val)

    res = await api.get(role.metadata.name)
    api.core.api.rbacv1.read_namespaced_role.assert_called_once_with(
        role.metadata.name, role.metadata.namespace, async_req=True
    )
    assert res == (role, None)


@pytest.mark.asyncio
async def test_role_list(role):
    api = RoleApi.new(namespace=DUMMY_NAMESPACE, config=MagicMock(Configuration), client=MagicMock(ApiClient))

    ret_val = asyncresult_return_value(V1RoleList(items=[role.dict()]))
    api.core.api.rbacv1.list_namespaced_role = MagicMock(return_value=ret_val)

    res = await api.list()
    api.core.api.rbacv1.list_namespaced_role.assert_called_once_with(role.metadata.namespace, async_req=True)
    assert res == ([role], None)
