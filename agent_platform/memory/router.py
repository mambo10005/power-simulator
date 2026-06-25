from fastapi import APIRouter
from sqlalchemy.orm import Session

from agent_platform.database.session import SessionLocal
from agent_platform.memory.service import MemoryService

router = APIRouter(
    prefix="/memory",
    tags=["Memory"]
)

service = MemoryService()

@router.post("/")
def store_memory(payload: dict):

    db: Session = SessionLocal()

    return service.store(
        db,
        payload
    )