import random
import string
from multiprocessing.pool import AsyncResult
from typing import Any
from unittest.mock import MagicMock

import pytest
from pydantic_factories import ModelFactory

from kubernetes_pydantic.types import metav1


DUMMY_NAMESPACE = "dummy"


def rand_str(length: int = 20) -> str:
    random.seed()
    return "".join(random.choices(string.ascii_letters + string.digits, k=length))


def asyncresult_return_value(val: Any) -> MagicMock:
    call = MagicMock(AsyncResult)
    call.get.return_value = val
    return call


@pytest.fixture
def meta() -> metav1.ObjectMeta:
    class Factory(ModelFactory):
        __model__ = metav1.ObjectMeta
        namespace = DUMMY_NAMESPACE
        name = rand_str()

    return Factory.build()
