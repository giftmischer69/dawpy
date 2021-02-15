from typing import Any

from pydantic import BaseModel
import pickledb


class Daw(BaseModel):
    def __init__(self, **data: Any):
        super().__init__(**data)
        self.db = pickledb.load("test.db", False)
