import asyncio
from typing import Any, Callable, Generic, Optional, Protocol, Type, TypeVar, Union

from kubernetes.client import ApiException
from pydantic import BaseModel

from kubernetes_pydantic.drivers.apicore import K8sApiCore

T = TypeVar("T", bound=BaseModel)


async def async_run(func: Callable):
    loop = asyncio.get_event_loop()
    return await loop.run_in_executor(None, func)


class K8sPyObj(Protocol):
    items: list

    def to_dict(self) -> dict:
        ...


class K8sWrapApi(Generic[T]):
    model: Type[T]
    core: K8sApiCore

    def __init__(self, core: K8sApiCore):
        self.core = core

    @staticmethod
    def to_dict(obj: Union[dict, K8sPyObj]) -> dict:
        if isinstance(obj, dict):
            return obj
        else:
            return obj.to_dict()

    @staticmethod
    def get_items(obj: Union[dict, K8sPyObj]) -> list:
        if isinstance(obj, dict):
            return obj["items"]
        else:
            return obj.items

    async def create_or_replace(self, name: str, body: T, **kwargs) -> tuple[Optional[T], Optional[ApiException]]:
        # NOTE This method is an alternative of server side apply which is not available in original kubernetes-python yet.
        curr, err = await self.get(name)
        if not curr:
            return await self.create(body, **kwargs)
        else:
            return await self.replace(name, body, **kwargs)

    async def create(self, body: T, **kwargs) -> tuple[Optional[T], Optional[ApiException]]:
        kwargs["async_req"] = True
        try:
            th = self.core.creator(*self.core.gvnk, body.dict(by_alias=True), **kwargs)
            res = await async_run(th.get)
        except ApiException as e:
            return None, e
        finally:
            self.core.close()

        obj: T = self.model.parse_obj(self.to_dict(res))
        return obj, None

    async def merge(self, name: str, body: T, **kwargs) -> tuple[Optional[T], Optional[ApiException]]:
        kwargs["async_req"] = True
        try:
            th = self.core.merger(*self.core.namespaced_name(name), body.dict(by_alias=True), **kwargs)
            res = await async_run(th.get)
        except ApiException as e:
            return None, e
        finally:
            self.core.close()

        obj: T = self.model.parse_obj(self.to_dict(res))
        return obj, None

    async def replace(self, name: str, body: T, **kwargs) -> tuple[Optional[T], Optional[ApiException]]:
        kwargs["async_req"] = True
        try:
            th = self.core.replacer(*self.core.namespaced_name(name), body.dict(by_alias=True), **kwargs)
            res = await async_run(th.get)
        except ApiException as e:
            return None, e
        finally:
            self.core.close()

        obj: T = self.model.parse_obj(self.to_dict(res))
        return obj, None

    async def delete(self, name: str, **kwargs) -> Optional[ApiException]:
        kwargs["async_req"] = True
        try:
            th = self.core.deleter(*self.core.namespaced_name(name), **kwargs)
            await async_run(th.get)
        except ApiException as e:
            return e
        finally:
            self.core.close()

        return None

    async def get(self, name: str, **kwargs) -> tuple[Optional[T], Optional[ApiException]]:
        kwargs["async_req"] = True
        try:
            th = self.core.getter(*self.core.namespaced_name(name), **kwargs)
            res = await async_run(th.get)
        except ApiException as e:
            return None, e
        finally:
            self.core.close()

        obj: T = self.model.parse_obj(self.to_dict(res))
        return obj, None

    async def list(self, **kwargs) -> tuple[list[T], Optional[ApiException]]:
        kwargs["async_req"] = True
        try:
            th = self.core.lister(*self.core.gvnk, **kwargs)
            res = await async_run(th.get)
        except ApiException as e:
            return [], e
        finally:
            self.core.close()

        return [self.model.parse_obj(self.to_dict(i)) for i in self.get_items(res)], None
