import logging

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


class User(db.Model, Base):
    __tablename__ = "users"

    id = db.Column(db.BigInteger, primary_key=True)
    uid = db.Column(db.String(50), unique=True)
    email = db.Column(db.String(256), unique=True)
    auth_token = db.Column(db.String(1024))

    def __unicode__(self):
        return f"{self.uid} - {self.email}"

    def __repr__(self):
        return f"<User {self.uid} - {self.email}>"

    meta = {
        "indexes": ["email", "uid"],
        # "ordering": ["-time"],
    }


class Business(db.Model, Base):
    __tablename__ = "businesses"

    id = db.Column(db.BigInteger, primary_key=True)
    name = db.Column(db.String(1024))
    industry = db.Column(db.String(50))
    pan = db.Column(db.String(10))
    gstin = db.Column(db.String(15))
    address = db.Column(db.String(1024))
    savings = db.Column(db.Numeric(10, 2))
    remaining_loan = db.Column(db.Numeric(10, 2))
    user_id = db.Column(db.BigInteger, db.ForeignKey("users.id"))
    user = db.relationship("User", back_populates="businesses", lazy=True)

    def __unicode__(self):
        return f"{self.id} - {self.name}"

    def __repr__(self):
        return f"<Business {self.id} - {self.name}"

    meta = {"indexes": ["industry"]}


class Deposit(db.Model, Base):
    __tablename__ = "deposits"

    id = db.Column(db.BigInteger, primary_key=True)
    amount = db.Column(db.Numeric(10, 2))
    business_id = db.Column(db.BigInteger, db.ForeignKey("businesses.id"))
    business = db.relationship("Business", back_populates="deposits", lazy=True)

    def __unicode__(self):
        return f"{self.id} - {self.amount}"

    def __repr__(self):
        return f"<Deposit {self.id} - {self.amount}"


class Loan(db.Model, Base):
    __tablename__ = "loans"

    id = db.Column(db.BigInteger, primary_key=True)
    amount = db.Column(db.Numeric(10, 2))
    term = db.Column(db.Integer)  # months
    business_id = db.Column(db.BigInteger, db.ForeignKey("businesses.id"))
    business = db.relationship("Business", back_populates="loans", lazy=True)

    def __unicode__(self):
        return f"{self.id} - {self.amount}"

    def __repr__(self):
        return f"<Deposit {self.id} - {self.amount}"
