from collections.abc import Callable

from cuid2 import cuid_wrapper
from pydantic import BaseModel, Field

__all__ = ["BaseObject"]


cuid_generator: Callable[[], str] = cuid_wrapper()


class BaseObject(BaseModel):
    id: str = Field(default_factory=cuid_generator)
