from fastapi import APIRouter
from sqlalchemy.orm import Session

from agent_platform.database.session import SessionLocal
from agent_platform.tasks.service import TaskService

router = APIRouter(
    prefix="/tasks",
    tags=["Tasks"]
)

service = TaskService()

@router.post("/")
def submit_task(payload: dict):

    db: Session = SessionLocal()

    return service.submit(
        db,
        payload
    )