import pytest
from app.crud import create_task, get_tasks
from app.schemas import TaskCreate
from app.database import connect_to_mongo, close_mongo_connection

@pytest.fixture
async def init_db():
    await connect_to_mongo()
    yield
    await close_mongo_connection()

@pytest.mark.anyio
async def test_create_task(init_db):
    task_data = TaskCreate(description="Test Task", status="Pending")
    task = await create_task(task_data)
    assert task.description == "Test Task"
    assert task.status == "Pending"

@pytest.mark.anyio
async def test_get_tasks(init_db):
    tasks = await get_tasks()
    assert isinstance(tasks, list)
