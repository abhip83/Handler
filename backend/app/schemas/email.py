from datetime import datetime

from pydantic import BaseModel, EmailStr, Field


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
    received_at: datetime