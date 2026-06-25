from fastapi import FastAPI

from agent_platform.database.base import Base
from agent_platform.database.session import engine

from agent_platform.registry.router import router as agent_router
from agent_platform.tasks.router import router as task_router
from agent_platform.memory.router import router as memory_router
from agent_platform.prompts.router import router as prompt_router

from agent_platform.registry.models import Agent
from agent_platform.tasks.models import Task
from agent_platform.memory.models import Memory
from agent_platform.prompts.models import Prompt

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Agent Platform"
)

app.include_router(agent_router)
app.include_router(task_router)
app.include_router(memory_router)
app.include_router(prompt_router)

@app.get("/")
def root():

    return {
        "status": "running"
    }