from model import Todo
from starlette.middleware.cors import CORSMiddleware
from fastapi import FastAPI, HTTPException

from .database import *

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


@app.get("/", tags=["root"])
async def read_root() -> dict:
    return {"message": "Welcome to your todo list."}


@app.get("/todo")
async def get_todo():
    response = await fetch_all_todos()
    return {"data": response}


@app.post("/todo", response_model=Todo)
async def post_todo(todo: Todo):
    response = await create_todo(todo.dict())
    if response:
        return response
    raise HTTPException(400, "Something went wrong")


@app.put("/todo/{id}", response_model=Todo)
async def put_todo(id: int, body: Todo) -> Todo:
    response = await update_todo(id, body)
    if response:
        return response
    raise HTTPException(404, f"There is no todo with the id {id}")


@app.delete("/todo/{id}")
async def delete_todo(id:int):
    response = await remove_todo(id)
    if response:
        return "Successfully deleted todo"
    raise HTTPException(404, f"There is no todo with the title {id}")
