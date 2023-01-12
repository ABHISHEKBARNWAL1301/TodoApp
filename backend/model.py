from pydantic import BaseModel, Field

class Todo(BaseModel):
    _id: int
    # id : int
    item: str
