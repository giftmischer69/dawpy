from typing import Any, Union, Optional, Callable

from pydantic import BaseModel
import pickledb
import json


class Daw(BaseModel):
    db: Any

    def __init__(self, **data: Any):
        super().__init__(**data)
        self.db = pickledb.load("test.db.json", True)

    def json(self, *, include: Union['AbstractSetIntStr', 'MappingIntStrAny'] = None,
             exclude: Union['AbstractSetIntStr', 'MappingIntStrAny'] = None, by_alias: bool = False,
             skip_defaults: bool = None, exclude_unset: bool = False, exclude_defaults: bool = False,
             exclude_none: bool = False, encoder: Optional[Callable[[Any], Any]] = None, **dumps_kwargs: Any) -> str:
        return json.dumps(str(self.db))
