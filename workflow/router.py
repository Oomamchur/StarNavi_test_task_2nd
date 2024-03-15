from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from dependencies import get_db
from workflow import schemas, crud

router = APIRouter()


@router.get("/workflows/", response_model=list[schemas.WorkFlow])
def list_workflows(
    skip: int = 0, limit: int = 100, db: Session = Depends(get_db)
):
    return crud.get_all_workflows(skip=skip, limit=limit, db=db)


@router.post("/workflows/", response_model=schemas.WorkFlow)
def create_workflow(
    workflow: schemas.WorkFlowCreate, db: Session = Depends(get_db)
):
    db_workflow = crud.get_workflow_by_name(db=db, name=workflow.name)
    if db_workflow:
        raise HTTPException(
            status_code=400, detail="This workflow is already exist in DB"
        )
    return crud.create_workflow(db=db, workflow=workflow)


@router.delete("/workflows/{workflow_id}", response_model=dict)
def delete_workflow_by_id(workflow_id: int, db: Session = Depends(get_db)):
    return crud.delete_workflow(db=db, workflow_id=workflow_id)