import motor.motor_asyncio
from model import Todo

client = motor.motor_asyncio.AsyncIOMotorClient('mongodb://localhost:27017')
database = client.Todo
collection = database.todo


async def fetch_all_todos():
    todos = []
    cursor = collection.find({})
    async for document in cursor:
        # print(**document.item)
        todos.append(Todo(**document))
    return todos


async def create_todo(todo):
    document = todo
    result = await collection.insert_one(document)
    return document


async def update_todo(id, item):
    await collection.update_one({"_id": id}, {"$set": {"item": item}})
    document = await collection.find_one({"_id": id})
    return document


async def remove_todo(id):
    await collection.delete_one({"_id": id})
    return True
