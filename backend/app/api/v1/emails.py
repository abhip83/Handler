from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.schemas.email import EmailCreate, EmailResponse
from app.services.email_service import EmailService

router = APIRouter(
    prefix="/emails",
    tags=["Emails"],
)


@router.post(
    "/",
    response_model=EmailResponse,
    status_code=201,
)
def create_email(
    email: EmailCreate,
    db: Session = Depends(get_db),
):
    service = EmailService(db)

    saved_email = service.process_email(email)

    return EmailResponse(
        id=saved_email.id,
        sender=saved_email.sender,
        recipient=saved_email.recipient,
        subject=saved_email.subject,
        body=saved_email.body,
        status=saved_email.status,
        category=saved_email.category,
        confidence=saved_email.confidence,

        customer_name=saved_email.customer_name,
        origin=saved_email.origin,
        destination=saved_email.destination,
        container_type=saved_email.container_type,
        cargo_description=saved_email.cargo_description,
        cargo_weight=saved_email.cargo_weight,
        quantity=saved_email.quantity,
        pickup_date=saved_email.pickup_date,
        delivery_date=saved_email.delivery_date,
        shipping_line=saved_email.shipping_line,
        incoterm=saved_email.incoterm,
        special_instructions=saved_email.special_instructions,
        action=saved_email.action,
        department=saved_email.department,
        priority=saved_email.priority,
        automation_level=saved_email.automation_level,
        decision_reason=saved_email.decision_reason,
        received_at=saved_email.received_at,
    )


@router.get(
    "/",
    response_model=list[EmailResponse],
)
def get_emails(
    db: Session = Depends(get_db),
):
    service = EmailService(db)

    return service.get_all()


@router.get(
    "/{email_id}",
    response_model=EmailResponse,
)
def get_email(
    email_id: str,
    db: Session = Depends(get_db),
):
    service = EmailService(db)

    email = service.get_by_id(email_id)

    if email is None:
        raise HTTPException(
            status_code=404,
            detail="Email not found",
        )

    return email