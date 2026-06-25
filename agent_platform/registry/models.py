from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String

from agent_platform.database.base import Base

class Agent(Base):

    __tablename__ = "agents"

    id = Column(Integer, primary_key=True)

    name = Column(String)

    role = Column(String)

    model = Column(String)

    status = Column(String)