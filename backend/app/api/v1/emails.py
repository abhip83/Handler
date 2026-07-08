from datetime import datetime, timezone
from uuid import uuid4

from fastapi import APIRouter, HTTPException

from app.schemas.email import EmailCreate, EmailResponse


router = APIRouter(
    prefix="/emails",
    tags=["Emails"]
)

emails_db: list[dict] = []


@router.post("", response_model=EmailResponse, status_code=201)
def create_email(email: EmailCreate):
    new_email = {
        "id": str(uuid4()),
        "sender": str(email.sender),
        "recipient": str(email.recipient),
        "subject": email.subject,
        "body": email.body,
        "status": "new",
        "received_at": datetime.now(timezone.utc),
    }

    emails_db.append(new_email)
    return new_email


@router.get("", response_model=list[EmailResponse])
def get_emails():
    return emails_db


@router.get("/{email_id}", response_model=EmailResponse)
def get_email(email_id: str):
    for email in emails_db:
        if email["id"] == email_id:
            return email

    raise HTTPException(
        status_code=404,
        detail="Email not found"
    )