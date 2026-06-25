from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String

from agent_platform.database.base import Base

class Task(Base):

    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True)

    agent_name = Column(String)

    task_type = Column(String)

    status = Column(String)

    prompt = Column(String)