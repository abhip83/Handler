from datetime import datetime, timezone
from uuid import uuid4

from sqlalchemy import DateTime, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column

from app.db.database import Base


class Workflow(Base):
    __tablename__ = "workflows"

    id: Mapped[str] = mapped_column(
        String,
        primary_key=True,
        default=lambda: str(uuid4()),
    )

    # Link to the processed email
    email_id: Mapped[str] = mapped_column(
        String,
        ForeignKey("emails.id"),
        nullable=False,
    )

    # Workflow execution state
    status: Mapped[str] = mapped_column(
        String,
        nullable=False,
        default="pending",
    )

    # Future: user assigned to handle this workflow
    assigned_to: Mapped[str | None] = mapped_column(
        String,
        nullable=True,
    )

    # Future: when someone starts working on it
    started_at: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True),
        nullable=True,
    )

    # Future: when workflow finishes
    completed_at: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True),
        nullable=True,
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc),
    )

    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc),
        onupdate=lambda: datetime.now(timezone.utc),
    )