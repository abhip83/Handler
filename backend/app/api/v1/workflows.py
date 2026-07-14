from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.schemas.workflow import (
    WorkflowResponse,
    WorkflowStatusUpdate,
)
from app.services.workflow_service import WorkflowService

router = APIRouter(
    prefix="/workflows",
    tags=["Workflows"],
)


@router.get(
    "/",
    response_model=list[WorkflowResponse],
)
def get_workflows(
    db: Session = Depends(get_db),
):
    service = WorkflowService(db)
    return service.get_all()


@router.get(
    "/{workflow_id}",
    response_model=WorkflowResponse,
)
def get_workflow(
    workflow_id: str,
    db: Session = Depends(get_db),
):
    service = WorkflowService(db)

    workflow = service.get_by_id(workflow_id)

    if workflow is None:
        raise HTTPException(
            status_code=404,
            detail="Workflow not found",
        )

    return workflow


@router.patch(
    "/{workflow_id}/status",
    response_model=WorkflowResponse,
)
def update_workflow_status(
    workflow_id: str,
    request: WorkflowStatusUpdate,
    db: Session = Depends(get_db),
):
    service = WorkflowService(db)

    workflow = service.update_status(
        workflow_id,
        request.status,
    )

    if workflow is None:
        raise HTTPException(
            status_code=404,
            detail="Workflow not found",
        )

    return workflow