# from pymongo.errors import ConnectionFailure
# from pymongo import MongoClient
# from model import db, Todo

# client = MongoClient("mongodb://localhost:27017/my")
# db = client["my"]
# collection = db["my"]





# @app.get("/")
# async def read_root():
#     return {"Hello": "World"}

# # for getting all todos

# # @app.get("/todo")
# # async def get_todos() -> dict:
# #     students = await db["my"].find().to_list(1000)
# #     return students


# @app.get("/todo")
# async def get_todos():
#     todos = []
#     async for student in collection.find():
#         todos.append(student)
#     return todos


# # @app.get("/items/{item_id}")
# # async def read_item(item_id: str):
# #     item = await collection.find_one({"_id": item_id})
# #     return item


# # for posting a todo item

# @app.post("/todo")
# async def add_todo(todo: dict):
#     result = await collection.insert_one(todo)
#     return result


from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


todos = [
    {
        "id": "1",
        "item": "Read a novel."
    },
    {
        "id": "2",
        "item": "Cycle around town."
    },
    {
        "id": "3",
        "item": "Have Lunch"
    }
]


app = FastAPI()

origins = [
    "http://localhost:3000",
    "localhost:3000"
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


@app.get("/", tags=["root"])
async def read_root() -> dict:
    return {"message": "Welcome to your todo list."}


@app.get("/todo", tags=["todos"])
async def get_todos() -> dict:
    return {"data": todos}


@app.post("/todo", tags=["todos"])
async def add_todo(todo: dict) -> dict:
    todos.append(todo)
    return {
        "data": {"Todo added."}
    }


@app.put("/todo/{id}", tags=["todos"])
async def update_todo(id: int, body: dict) -> dict:
    for todo in todos:
        if int(todo["id"]) == id:
            todo["item"] = body["item"]
            return {
                "data": f"Todo with id {id} has been updated."
            }

    return {
        "data": f"Todo with id {id} not found."
    }


@app.delete("/todo/{id}", tags=["todos"])
async def delete_todo(id: int) -> dict:
    for todo in todos:
        if int(todo["id"]) == id:
            todos.remove(todo)
            return {
                "data": f"Todo with id {id} has been removed."
            }

    return {
        "data": f"Todo with id {id} not found."
    }
