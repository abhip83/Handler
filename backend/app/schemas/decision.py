from enum import Enum

from pydantic import BaseModel, Field


class Priority(str, Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"


class AutomationLevel(str, Enum):
    AUTOMATIC = "automatic"
    HUMAN_REVIEW = "human_review"


class Department(str, Enum):
    SALES = "Sales"
    OPERATIONS = "Operations"
    DOCUMENTATION = "Documentation"
    SUPPORT = "Support"


class WorkflowAction(str, Enum):
    GENERATE_QUOTE = "generate_quote"
    CREATE_BOOKING = "create_booking"
    CHECK_TRACKING = "check_tracking"
    REQUEST_DOCUMENTS = "request_documents"
    MANUAL_REVIEW = "manual_review"


class DecisionResult(BaseModel):
    """
    Represents the business decision made after
    email classification and shipment extraction.
    """

    action: WorkflowAction = Field(
        ...,
        description="Workflow action to be executed."
    )

    department: Department = Field(
        ...,
        description="Department responsible for handling the email."
    )

    priority: Priority = Field(
        ...,
        description="Business priority assigned to the email."
    )

    automation_level: AutomationLevel = Field(
        ...,
        description="Whether the workflow can be automated or requires human review."
    )

    reason: str = Field(
        ...,
        description="Human-readable explanation of why the decision was made."
    )