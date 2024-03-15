from fastapi import HTTPException
from sqlalchemy import delete

from workflow import models
from sqlalchemy.orm import Session

from workflow.schemas import WorkFlowCreate


def get_all_workflows(
    db: Session, skip: int, limit: int
) -> list[models.WorkFlow]:
    return db.query(models.WorkFlow).offset(skip).limit(limit).all()


def get_workflow_by_id(db: Session, workflow_id: int) -> models.WorkFlow:
    return (
        db.query(models.WorkFlow)
        .filter(models.WorkFlow.id == workflow_id)
        .first()
    )


def get_workflow_by_name(db: Session, name: str) -> models.WorkFlow:
    return (
        db.query(models.WorkFlow).filter(models.WorkFlow.name == name).first()
    )


def create_workflow(db: Session, workflow: WorkFlowCreate) -> models.WorkFlow:
    db_workflow = models.WorkFlow(
        name=workflow.name, description=workflow.description
    )
    db.add(db_workflow)
    db.commit()
    db.refresh(db_workflow)

    return db_workflow


def update_workflow(db: Session):
    pass


def delete_workflow(db: Session, workflow_id: int) -> dict:
    db_workflow = get_workflow_by_id(db=db, workflow_id=workflow_id)
    if db_workflow:
        query = delete(models.WorkFlow).where(
            models.WorkFlow.id == workflow_id
        )
        db.execute(query)
        db.commit()
        return {"message": "Deleted successfully"}

    raise HTTPException(status_code=404, detail="WorkFlow not found")
