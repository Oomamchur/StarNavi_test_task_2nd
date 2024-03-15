from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from database import Base
from node.models import Node


class WorkFlow(Base):
    __tablename__ = "workflow"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(80), nullable=False, unique=True)
    description = Column(String(500), nullable=True)
    node_id = Column(Integer, ForeignKey("node.id"))

    node = relationship(Node, lazy="selectin")
