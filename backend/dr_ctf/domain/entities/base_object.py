from uuid import UUID, uuid4

from pydantic import BaseModel, Field

__all__ = ["BaseObject"]


class BaseObject(BaseModel):
    id: UUID = Field(default_factory=uuid4)
