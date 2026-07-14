from app.models.workflow import Workflow
from app.repositories.workflow_repository import WorkflowRepository


class WorkflowService:

    def __init__(self, db):
        self.db = db

    def create_workflow(self, email_id: str):

        workflow = Workflow(
            email_id=email_id,
            status="pending",
        )

        return WorkflowRepository.create(
            self.db,
            workflow,
        )

    def get_all(self):
        return WorkflowRepository.get_all(self.db)

    def get_by_id(self, workflow_id):
        return WorkflowRepository.get_by_id(
            self.db,
            workflow_id,
        )

    def update_status(
        self,
        workflow_id: str,
        status: str,
    ):

        workflow = self.get_by_id(workflow_id)

        if workflow is None:
            return None

        return WorkflowRepository.update_status(
            self.db,
            workflow,
            status,
        )