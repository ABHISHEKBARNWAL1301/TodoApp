import motor.motor_asyncio
from model import Todo

client = motor.motor_asyncio.AsyncIOMotorClient('mongodb://localhost:27017')
database = client.Todo
collection = database.todo


async def fetch_all_todos():
    todos = []
    cursor = collection.find({},{'_id' : 0})
    async for document in cursor:
        todos.append(Todo(**document))
    return todos


async def create_todo(todo):
    document = todo
    result = await collection.insert_one(document)
    return result


async def update_todo(id, todo):
    await collection.update_one({"id": id}, {"$set": {"item": todo.item}})
    document = await collection.find_one({"id": id})
    return document


async def remove_todo(id):
    await collection.delete_one({"id": id})
    return True
