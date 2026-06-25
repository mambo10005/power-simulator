from fastapi import APIRouter
from sqlalchemy.orm import Session

from agent_platform.database.session import SessionLocal
from agent_platform.registry.service import AgentService

router = APIRouter(
    prefix="/agents",
    tags=["Agents"]
)

service = AgentService()

@router.post("/")
def create_agent(payload: dict):

    db: Session = SessionLocal()

    return service.create_agent(
        db,
        payload
    )