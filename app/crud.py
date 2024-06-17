from app.database import db
from app.models import TaskModel
from app.schemas import TaskCreate

async def create_task(task: TaskCreate) -> TaskModel:
    task = TaskModel(**task.dict())
    result = await db["tasks"].insert_one(task.dict())
    task.id = result.inserted_id
    return task

async def get_tasks() -> list[TaskModel]:
    tasks = await db["tasks"].find().to_list(1000)
    return tasks
