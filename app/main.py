from fastapi import FastAPI, HTTPException
from app.schemas import TaskCreate, TaskResponse
from app.crud import create_task, get_tasks
from app.database import connect_to_mongo, close_mongo_connection

app = FastAPI()

@app.on_event("startup")
async def startup_db_client():
    await connect_to_mongo()

@app.on_event("shutdown")
async def shutdown_db_client():
    await close_mongo_connection()

@app.post("/tasks/", response_model=TaskResponse)
async def create_new_task(task: TaskCreate):
    task = await create_task(task)
    return task

@app.get("/tasks/", response_model=list[TaskResponse])
async def read_tasks():
    tasks = await get_tasks()
    return tasks