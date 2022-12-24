from slick.model import BaseModel, get_engine
from sqlalchemy import Column, Date, ForeignKey, Integer, String, Time
from sqlalchemy.orm import backref, relationship


class Person(BaseModel):
    __tablename__ = "person"
    _lookup_attributes = ('id', )

    id = Column(Integer, primary_key=True)
    birth_year = Column(Integer)
    bookings = relationship("Booking", backref=backref("person"))
    cases = relationship("Case", backref=backref("person"))


class Booking(BaseModel):
    __tablename__ = "booking"
    _lookup_attributes = ('id', )

    id = Column(Integer, primary_key=True)
    person_id = Column(Integer, ForeignKey("person.id"))
    admission_date = Column(Date)
    release_date = Column(Date)


class Arrest(BaseModel):
    __tablename__ = "arrest"
    _lookup_attributes = ('case_id', 'person_id', 'agency', 'arrest_date')

    id = Column(Integer, primary_key=True)
    person_id = Column(Integer, ForeignKey("person.id"))
    case_id = Column(String, ForeignKey("case.case_id"))
    arrest_date = Column(Date)
    agency = Column(String)
    location = Column(String)
    officer = Column(String)


class Charge(BaseModel):
    __tablename__ = "charge"
    _lookup_attributes = ('case_id', 'statute')

    id = Column(Integer, primary_key=True)
    case_id = Column(String, ForeignKey("case.case_id"))
    charge_type = Column(String)
    statute = Column(String)
    description = Column(String)


class Warrant(BaseModel):
    __tablename__ = "warrant"
    _lookup_attributes = ('case_id', 'description')

    id = Column(Integer, primary_key=True)
    case_id = Column(String, ForeignKey("case.case_id"))
    warrant_type = Column(String)
    description = Column(String)


class Bond(BaseModel):
    __tablename__ = "bond"
    _lookup_attributes = ('case_id', 'bond_type')

    id = Column(Integer, primary_key=True)
    case_id = Column(String, ForeignKey("case.case_id"))
    bond_type = Column(String)
    amount = Column(Integer)
    paid_date = Column(Date)
    release_type = Column(String)
    release_date = Column(Date)
    judge = Column(String)


class Case(BaseModel):
    __tablename__ = "case"
    _lookup_attributes = ('case_id', 'person_id')

    id = Column(Integer, primary_key=True)
    case_id = Column(String, nullable=False)
    person_id = Column(Integer, ForeignKey("person.id"), nullable=False)
    arrests = relationship("Arrest", backref=backref("case"))
    charges = relationship("Charge", backref=backref("case"))
    warrants = relationship("Warrant", backref=backref("case"))
    bonds = relationship("Bond", backref=backref("case"))
