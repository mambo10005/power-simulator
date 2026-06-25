from fastapi import APIRouter
from sqlalchemy.orm import Session

from agent_platform.database.session import SessionLocal
from agent_platform.prompts.service import PromptService

router = APIRouter(
    prefix="/prompts",
    tags=["Prompts"]
)

service = PromptService()

@router.post("/")
def create_prompt(payload: dict):

    db: Session = SessionLocal()

    return service.create(
        db,
        payload
    )