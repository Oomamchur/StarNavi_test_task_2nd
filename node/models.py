from enum import StrEnum, auto

from sqlalchemy import Column, Integer, String, Enum

from database import Base


class NodeType(StrEnum):
    START_NODE = auto()
    MESSAGE_NODE = auto()
    CONDITION_NODE = auto()
    END_NODE = auto()


class Node(Base):
    __tablename__ = "node"

    id = Column(Integer, primary_key=True, index=True)
    type = Column(Enum(NodeType), nullable=False, unique=True)
    description = Column(String(500), nullable=True)
