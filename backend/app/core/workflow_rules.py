from app.schemas.decision import (
    AutomationLevel,
    DecisionResult,
    Department,
    Priority,
    WorkflowAction,
)

WORKFLOW_RULES = {
    "quote_request": DecisionResult(
        action=WorkflowAction.GENERATE_QUOTE,
        department=Department.SALES,
        priority=Priority.HIGH,
        automation_level=AutomationLevel.AUTOMATIC,
        reason="Customer requested freight pricing.",
    ),

    "booking_request": DecisionResult(
        action=WorkflowAction.CREATE_BOOKING,
        department=Department.OPERATIONS,
        priority=Priority.HIGH,
        automation_level=AutomationLevel.HUMAN_REVIEW,
        reason="Customer requested shipment booking.",
    ),

    "shipment_status": DecisionResult(
        action=WorkflowAction.CHECK_TRACKING,
        department=Department.OPERATIONS,
        priority=Priority.MEDIUM,
        automation_level=AutomationLevel.AUTOMATIC,
        reason="Customer requested shipment status.",
    ),

    "document_request": DecisionResult(
        action=WorkflowAction.REQUEST_DOCUMENTS,
        department=Department.DOCUMENTATION,
        priority=Priority.MEDIUM,
        automation_level=AutomationLevel.HUMAN_REVIEW,
        reason="Customer requested shipping documents.",
    ),

    "unrelated": DecisionResult(
        action=WorkflowAction.MANUAL_REVIEW,
        department=Department.SUPPORT,
        priority=Priority.LOW,
        automation_level=AutomationLevel.HUMAN_REVIEW,
        reason="Email does not match any logistics workflow.",
    ),
}