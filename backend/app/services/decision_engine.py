from app.core.workflow_rules import WORKFLOW_RULES
from app.schemas.decision import (
    AutomationLevel,
    DecisionResult,
    Department,
    Priority,
    WorkflowAction,
)


class DecisionEngine:
    """
    Determines the business workflow after
    email classification and information extraction.
    """

    def decide(self, category: str) -> DecisionResult:
        """
        Returns the workflow decision for the
        classified email category.
        """

        return WORKFLOW_RULES.get(
            category,
            DecisionResult(
                action=WorkflowAction.MANUAL_REVIEW,
                department=Department.SUPPORT,
                priority=Priority.LOW,
                automation_level=AutomationLevel.HUMAN_REVIEW,
                reason="Unknown email category.",
            ),
        )