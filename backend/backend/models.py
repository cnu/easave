import logging
from dataclasses import dataclass

from backend.extensions import db
from sqlalchemy import exc, MetaData, Numeric, ForeignKey
from sqlalchemy.orm import (
    DeclarativeBase,
    MappedAsDataclass,
    mapped_column,
    Mapped,
    relationship,
)
from typing_extensions import Annotated

log = logging.getLogger(__name__)


class Base:
    created_at = db.Column(db.DateTime, default=db.func.now())
    updated_at = db.Column(db.DateTime, default=db.func.now(), onupdate=db.func.now())

    def save(self, commit=True):
        db.session.add(self)
        if commit:
            try:
                db.session.commit()
                return self
            except exc.SQLAlchemyError as e:
                log.error(e)
                db.session.rollback()
                return None

    def delete(self, commit=True):
        db.session.delete(self)
        if commit:
            try:
                db.session.commit()
                return self
            except exc.SQLAlchemyError as e:
                log.error(e)
                db.session.rollback()
                return None


@dataclass
class User(db.Model, Base):
    __tablename__ = "users"

    id: Mapped[int] = db.Column(
        db.BigInteger().with_variant(db.Integer, "sqlite"), primary_key=True
    )
    uid: Mapped[str] = db.Column(db.String(50), unique=True)
    email: Mapped[str] = db.Column(db.String(256), unique=True)

    def __unicode__(self):
        return f"{self.uid} - {self.email}"

    def __repr__(self):
        return f"<User {self.uid} - {self.email}>"

    meta = {
        "indexes": ["email", "uid"],
        # "ordering": ["-time"],
    }


@dataclass
class Business(db.Model, Base):
    __tablename__ = "businesses"

    id: Mapped[int] = db.Column(
        db.BigInteger().with_variant(db.Integer, "sqlite"), primary_key=True
    )
    name: Mapped[str] = db.Column(db.String(1024))
    industry: Mapped[str] = db.Column(db.String(50))
    pan: Mapped[str] = db.Column(db.String(10))
    gstin: Mapped[str] = db.Column(db.String(15))
    address: Mapped[str] = db.Column(db.String(1024))
    savings: Mapped[float] = db.Column(db.Numeric(10, 2))
    remaining_loan: Mapped[float] = db.Column(db.Numeric(10, 2))
    user_id = db.Column(db.BigInteger, db.ForeignKey("users.id"))
    user: Mapped["User"] = db.relationship("User", backref="businesses", lazy=True)

    def __unicode__(self):
        return f"{self.id} - {self.name}"

    def __repr__(self):
        return f"<Business {self.id} - {self.name}"

    meta = {"indexes": ["industry"]}


@dataclass
class Deposit(db.Model, Base):
    __tablename__ = "deposits"

    id: Mapped[int] = db.Column(
        db.BigInteger().with_variant(db.Integer, "sqlite"), primary_key=True
    )
    amount: Mapped[float] = db.Column(db.Numeric(10, 2))
    business_id = db.Column(db.BigInteger, db.ForeignKey("businesses.id"))
    business: Mapped["Business"] = db.relationship(
        "Business", backref="deposits", lazy=True
    )

    def __unicode__(self):
        return f"{self.id} - {self.amount}"

    def __repr__(self):
        return f"<Deposit {self.id} - {self.amount}"


@dataclass
class Loan(db.Model, Base):
    __tablename__ = "loans"

    id: Mapped[int] = db.Column(
        db.BigInteger().with_variant(db.Integer, "sqlite"), primary_key=True
    )
    amount: Mapped[float] = db.Column(db.Numeric(10, 2))
    term: Mapped[int] = db.Column(db.Integer)  # months
    business_id = db.Column(db.BigInteger, db.ForeignKey("businesses.id"))
    business: Mapped["Business"] = db.relationship(
        "Business", backref="loans", lazy=True
    )

    def __unicode__(self):
        return f"{self.id} - {self.amount}"

    def __repr__(self):
        return f"<Deposit {self.id} - {self.amount}"
