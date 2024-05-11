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


class Base(DeclarativeBase, MappedAsDataclass):
    created_at = db.Column(db.DateTime, default=db.func.now())
    updated_at = db.Column(db.DateTime, default=db.func.now(), onupdate=db.func.now())

    metadata = MetaData(
        naming_convention={
            "ix": "ix_%(column_0_label)s",
            "uq": "uq_%(table_name)s_%(column_0_name)s",
            "ck": "ck_%(table_name)s_%(constraint_name)s",
            "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
            "pk": "pk_%(table_name)s",
        }
    )

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


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    uid: Mapped[str] = mapped_column(unique=True)
    email: Mapped[str] = mapped_column(unique=True)
    auth_token: Mapped[str]

    def __unicode__(self):
        return f"{self.uid} - {self.email}"

    def __repr__(self):
        return f"<User {self.uid} - {self.email}>"

    meta = {
        "indexes": ["email", "uid"],
        # "ordering": ["-time"],
    }


user_fk = Annotated[int, mapped_column(ForeignKey("users.id"))]


class Business(Base):
    __tablename__ = "businesses"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    industry: Mapped[str]
    savings: Mapped[float] = mapped_column(Numeric(10, 2))
    loan: Mapped[float] = mapped_column(Numeric(10, 2))
    user_id: Mapped[user_fk] = mapped_column(init=False)
    user: Mapped["User"] = relationship(back_populates="businesses", default=None)

    def __unicode__(self):
        return f"{self.id} - {self.name}"

    def __repr__(self):
        return f"<Business {self.id} - {self.name}"

    meta = {"indexes": ["industry"]}


business_fk = Annotated[int, mapped_column(ForeignKey("businesses.id"))]


class Deposit(Base):
    __tablename__ = "deposits"

    id: Mapped[int] = mapped_column(primary_key=True)
    amount: Mapped[float] = mapped_column(Numeric(10, 2))
    business_id: Mapped[business_fk] = mapped_column(init=False)
    business: Mapped["Business"] = relationship(back_populates="deposits", default=None)

    def __unicode__(self):
        return f"{self.id} - {self.amount}"

    def __repr__(self):
        return f"<Deposit {self.id} - {self.amount}"


class Loan(Base):
    __tablename__ = "loans"

    id: Mapped[int] = mapped_column(primary_key=True)
    amount: Mapped[float] = mapped_column(Numeric(10, 2))
    term: Mapped[int]  # months
    business_id: Mapped[business_fk] = mapped_column(init=False)
    business: Mapped["Business"] = relationship(back_populates="deposits", default=None)

    def __unicode__(self):
        return f"{self.id} - {self.amount}"

    def __repr__(self):
        return f"<Deposit {self.id} - {self.amount}"
