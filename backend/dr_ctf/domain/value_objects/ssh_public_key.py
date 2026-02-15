from pydantic import BaseModel, FilePath


class SshPublicKey(BaseModel):
    # TODO: Figure out what we need for this
    file: FilePath
