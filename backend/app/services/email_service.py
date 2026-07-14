from uuid import uuid4
from datetime import datetime, timezone

from app.models.email import Email
from app.repositories.email_repository import EmailRepository
from app.services.classifier import classify_email
from app.services.decision_engine import DecisionEngine
from app.services.extractor import extract_shipment_information
from app.services.workflow_service import WorkflowService


class EmailService:

    def __init__(self, db):
        self.db = db
        self.decision_engine = DecisionEngine()
        self.workflow_service = WorkflowService(db)

    def process_email(self, email):

        # STEP 1: Classify email
        classification = classify_email(
            subject=email.subject,
            body=email.body,
        )

        # STEP 2: Extract shipment information
        shipment = extract_shipment_information(
            subject=email.subject,
            body=email.body,
        )

        # STEP 3: Make business decision
        decision = self.decision_engine.decide(
            classification.category.value
        )

        print("========== AI DECISION ==========")
        print(decision.model_dump())
        print("================================")

        # STEP 4: Build Email ORM object
        db_email = Email(
            id=str(uuid4()),

            sender=str(email.sender),
            recipient=str(email.recipient),

            subject=email.subject,
            body=email.body,

            status="classified",

            category=classification.category.value,
            confidence=classification.confidence,

            # AI Extracted Shipment Fields
            customer_name=shipment.customer_name,
            origin=shipment.origin,
            destination=shipment.destination,
            container_type=shipment.container_type,
            cargo_description=shipment.cargo_description,
            cargo_weight=shipment.cargo_weight,
            quantity=shipment.quantity,
            pickup_date=shipment.pickup_date,
            delivery_date=shipment.delivery_date,
            shipping_line=shipment.shipping_line,
            incoterm=shipment.incoterm,
            special_instructions=shipment.special_instructions,

            # AI Decision Fields
            action=decision.action.value,
            department=decision.department.value,
            priority=decision.priority.value,
            automation_level=decision.automation_level.value,
            decision_reason=decision.reason,

            received_at=datetime.now(timezone.utc),
        )

        # STEP 5: Save email
        saved_email = EmailRepository.create(
            self.db,
            db_email,
        )

        # STEP 6: Automatically create workflow
        workflow = self.workflow_service.create_workflow(
            email_id=saved_email.id,
        )

        print("========== WORKFLOW CREATED ==========")
        print(f"Workflow ID: {workflow.id}")
        print(f"Status: {workflow.status}")
        print("======================================")

        return saved_email

    def get_all(self):
        return EmailRepository.get_all(self.db)

    def get_by_id(self, email_id):
        return EmailRepository.get_by_id(
            self.db,
            email_id,
        )