#! /usr/bin/env python3

from pydantic import BaseModel, StrictInt

class Todo(BaseModel):
    id: StrictInt
    item: str
