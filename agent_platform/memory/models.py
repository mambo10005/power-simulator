from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String

from agent_platform.database.base import Base

class Memory(Base):

    __tablename__ = "memory"

    id = Column(Integer, primary_key=True)

    agent_name = Column(String)

    key = Column(String)

    value = Column(String)