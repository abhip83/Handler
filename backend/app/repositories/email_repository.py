from sqlalchemy.orm import Session

from app.models.email import Email


class EmailRepository:

    @staticmethod
    def create(db: Session, email: Email):
        db.add(email)
        db.commit()
        db.refresh(email)
        return email

    @staticmethod
    def get_all(db: Session):
        return db.query(Email).all()

    @staticmethod
    def get_by_id(db: Session, email_id: str):
        return (
            db.query(Email)
            .filter(Email.id == email_id)
            .first()
        )