from typing import Any

from pydantic import BaseModel
import pickledb
import json


class Daw(BaseModel):
    db: Any

    def __init__(self, **data: Any):
        super().__init__(**data)
        self.db = pickledb.load("test.db.json", True)

    def json(self, *args, **kwargs) -> str:
        return json.dumps(str(self.db))


""" 
Pattern: 
        StaccatoProducer(Midi: Produces a midi with jfugue) 
        + WavProducer(Plugin: Produces Wav with a midi (dll+fxp)) 
"""
