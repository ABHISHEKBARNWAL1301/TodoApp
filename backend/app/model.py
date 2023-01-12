from pydantic import BaseModel
from bson import ObjectId

class Todo(BaseModel):
    id : int
    items : str
