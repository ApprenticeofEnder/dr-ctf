from typing import Annotated

from pydantic import BaseModel, Field

PortValue = Annotated[int, Field(gt=0, lt=65536)]


class Port(BaseModel):
    value: PortValue
    description: str


class HttpPort(BaseModel):
    value: PortValue = 80
    description: str = "HTTP"


class HttpsPort(BaseModel):
    value: PortValue = 443
    description: str = "HTTPS"


class SshPort(BaseModel):
    value: PortValue = 22
    description: str = "SSH"
