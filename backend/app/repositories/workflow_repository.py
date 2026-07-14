from datetime import datetime, timezone

from sqlalchemy.orm import Session

from app.models.workflow import Workflow


class WorkflowRepository:

    @staticmethod
    def create(db: Session, workflow: Workflow) -> Workflow:
        db.add(workflow)
        db.commit()
        db.refresh(workflow)
        return workflow

    @staticmethod
    def get_all(db: Session):
        return (
            db.query(Workflow)
            .order_by(Workflow.created_at.desc())
            .all()
        )

    @staticmethod
    def get_by_id(db: Session, workflow_id: str):
        return (
            db.query(Workflow)
            .filter(Workflow.id == workflow_id)
            .first()
        )

    @staticmethod
    def update_status(
        db: Session,
        workflow: Workflow,
        status: str,
    ):

        workflow.status = status

        if status == "in_progress" and workflow.started_at is None:
            workflow.started_at = datetime.now(timezone.utc)

        if status == "completed":
            workflow.completed_at = datetime.now(timezone.utc)

        db.commit()
        db.refresh(workflow)

        return workflow