from pydantic import BaseModel


class WorkFlowBase(BaseModel):
    name: str
    description: str


class WorkFlowCreate(WorkFlowBase):
    pass


class WorkFlowUpdate(WorkFlowBase):
    pass


class WorkFlow(WorkFlowBase):
    id: int

    class Config:
        from_attributes = True
