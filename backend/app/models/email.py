from datetime import datetime, timezone

from sqlalchemy import String, Text, Float, DateTime
from sqlalchemy.orm import Mapped, mapped_column

from app.db.database import Base


class Email(Base):
    __tablename__ = "emails"

    id: Mapped[str] = mapped_column(
        String,
        primary_key=True,
    )

    sender: Mapped[str] = mapped_column(
        String,
        nullable=False,
    )

    recipient: Mapped[str] = mapped_column(
        String,
        nullable=False,
    )

    subject: Mapped[str] = mapped_column(
        String,
        nullable=False,
    )

    body: Mapped[str] = mapped_column(
        Text,
        nullable=False,
    )

    status: Mapped[str] = mapped_column(
        String,
        nullable=False,
        default="classified",
    )

    category: Mapped[str] = mapped_column(
        String,
        nullable=False,
    )

    confidence: Mapped[float] = mapped_column(
        Float,
        nullable=False,
    )

    # ==============================
    # AI Extracted Shipment Fields
    # ==============================

    customer_name: Mapped[str | None] = mapped_column(
        String,
        nullable=True,
    )

    origin: Mapped[str | None] = mapped_column(
        String,
        nullable=True,
    )

    destination: Mapped[str | None] = mapped_column(
        String,
        nullable=True,
    )

    container_type: Mapped[str | None] = mapped_column(
        String,
        nullable=True,
    )

    cargo_description: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    cargo_weight: Mapped[str | None] = mapped_column(
        String,
        nullable=True,
    )

    quantity: Mapped[str | None] = mapped_column(
        String,
        nullable=True,
    )

    pickup_date: Mapped[str | None] = mapped_column(
        String,
        nullable=True,
    )

    delivery_date: Mapped[str | None] = mapped_column(
        String,
        nullable=True,
    )

    shipping_line: Mapped[str | None] = mapped_column(
        String,
        nullable=True,
    )

    incoterm: Mapped[str | None] = mapped_column(
        String,
        nullable=True,
    )

    special_instructions: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    # ==============================
    # AI Decision Engine Fields
    # ==============================

    action: Mapped[str | None] = mapped_column(
        String,
        nullable=True,
    )

    department: Mapped[str | None] = mapped_column(
        String,
        nullable=True,
    )

    priority: Mapped[str | None] = mapped_column(
        String,
        nullable=True,
    )

    automation_level: Mapped[str | None] = mapped_column(
        String,
        nullable=True,
    )

    decision_reason: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    received_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        default=lambda: datetime.now(timezone.utc),
    )