from pydantic import BaseModel, Field


class Todo(BaseModel):
    id: int = Field(None, alias="id")
    item: str = Field(None, alias="item")
