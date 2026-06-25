from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String

from agent_platform.database.base import Base

class Prompt(Base):

    __tablename__ = "prompts"

    id = Column(Integer, primary_key=True)

    name = Column(String)

    content = Column(String)