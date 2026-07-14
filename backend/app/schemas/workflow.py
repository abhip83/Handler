from datetime import datetime

from pydantic import BaseModel


class WorkflowStatusUpdate(BaseModel):
    status: str


class WorkflowResponse(BaseModel):
    id: str
    email_id: str

    status: str

    assigned_to: str | None = None

    started_at: datetime | None = None
    completed_at: datetime | None = None

    created_at: datetime
    updated_at: datetime

    model_config = {
        "from_attributes": True
    }