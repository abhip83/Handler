from datetime import datetime

from pydantic import BaseModel, EmailStr, Field

from app.schemas.classification import EmailCategory


class EmailCreate(BaseModel):
    sender: EmailStr = Field(alias="from")
    recipient: EmailStr = Field(alias="to")
    subject: str
    body: str

    model_config = {
        "populate_by_name": True
    }


class EmailResponse(BaseModel):
    id: str
    sender: EmailStr
    recipient: EmailStr

    subject: str
    body: str

    status: str

    category: EmailCategory
    confidence: float

    # ==============================
    # AI Extracted Shipment Fields
    # ==============================

    customer_name: str | None = None
    origin: str | None = None
    destination: str | None = None
    container_type: str | None = None
    cargo_description: str | None = None
    cargo_weight: str | None = None
    quantity: str | None = None
    pickup_date: str | None = None
    delivery_date: str | None = None
    shipping_line: str | None = None
    incoterm: str | None = None
    special_instructions: str | None = None

    # ==============================
    # AI Decision Engine Fields
    # ==============================

    action: str | None = None
    department: str | None = None
    priority: str | None = None
    automation_level: str | None = None
    decision_reason: str | None = None

    received_at: datetime

    model_config = {
        "from_attributes": True
    }