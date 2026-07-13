from pydantic import BaseModel
from typing import Optional


class ShipmentExtraction(BaseModel):
    customer_name: Optional[str] = None

    origin: Optional[str] = None
    destination: Optional[str] = None

    container_type: Optional[str] = None

    cargo_description: Optional[str] = None
    cargo_weight: Optional[str] = None
    quantity: Optional[str] = None

    pickup_date: Optional[str] = None
    delivery_date: Optional[str] = None

    shipping_line: Optional[str] = None
    incoterm: Optional[str] = None

    special_instructions: Optional[str] = None

    confidence: float