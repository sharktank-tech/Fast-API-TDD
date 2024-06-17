from pydantic import BaseModel

class TaskCreate(BaseModel):
    description: str
    status: str

class TaskResponse(TaskCreate):
    id: str