from enum import Enum

from pydantic import BaseModel, Field


class EmailCategory(str, Enum):
    QUOTE_REQUEST = "quote_request"
    SHIPMENT_STATUS = "shipment_status"
    BOOKING_REQUEST = "booking_request"
    DOCUMENT_REQUEST = "document_request"
    UNRELATED = "unrelated"


class ClassificationResult(BaseModel):
    category: EmailCategory
    confidence: float = Field(ge=0.0, le=1.0)