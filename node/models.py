from enum import auto, StrEnum

from sqlalchemy import Column, Integer, String, ForeignKey, Enum
from sqlalchemy.orm import relationship

from database import Base
from workflow.models import WorkFlow


class NodeType(StrEnum):
    START_NODE = "START_NODE"
    MESSAGE_NODE = "MESSAGE_NODE"
    CONDITION_NODE = "CONDITION_NODE"
    END_NODE = "END_NODE"


class Node(Base):
    __tablename__ = "node"

    id = Column(Integer, primary_key=True, index=True)
    type = Column(Enum(NodeType), nullable=False, unique=True)
    text = Column(String(500), nullable=True)
    workflow_id = Column(Integer, ForeignKey("workflow.id"))

    workflow = relationship(WorkFlow, lazy="selectin")
