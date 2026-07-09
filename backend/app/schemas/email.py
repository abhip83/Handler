from datetime import datetime

from pydantic import BaseModel, EmailStr, Field

from app.schemas.classification import EmailCategory


class EmailCreate(BaseModel):
    sender: EmailStr = Field(alias="from")
    recipient: EmailStr = Field(alias="to")
    subject: str
    body: str


class EmailResponse(BaseModel):
    id: str
    sender: EmailStr
    recipient: EmailStr
    subject: str
    body: str
    status: str
    category: EmailCategory
    confidence: float
    received_at: datetime