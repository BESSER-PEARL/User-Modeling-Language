import enum
from typing import List, Optional
from sqlalchemy import (
    create_engine, Column, ForeignKey, Table, Text, Boolean, String, Date, 
    Time, DateTime, Float, Integer, Enum
)
from sqlalchemy.orm import (
    column_property, DeclarativeBase, Mapped, mapped_column, relationship
)
from datetime import datetime, time, date

class Base(DeclarativeBase):
    pass

# Enum definitions

class CEFR(enum.Enum):
    
    B2 = "B2"
    C1 = "C1"
    A2 = "A2"
    C2 = "C2"
    A1 = "A1"
    B1 = "B1"



# Tables definition for many-to-many relationships

# Tables definition
class Nationality(Base):
    
    __tablename__ = "nationality"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100))

class Interest(Base):
    
    __tablename__ = "interest"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100))

class User(Base):
    
    __tablename__ = "user"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100))

class Age(Base):
    
    __tablename__ = "age"
    id: Mapped[int] = mapped_column(primary_key=True)
    value: Mapped[int] = mapped_column(Integer)

class Hobby(Base):
    
    __tablename__ = "hobby"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100))

class StaticProperty(Base):
    
    __tablename__ = "staticproperty"
    id: Mapped[int] = mapped_column(primary_key=True)
    type_spec: Mapped[str]
    __mapper_args__ = {
        "polymorphic_identity": "staticproperty",
        "polymorphic_on": "type_spec",
    }

class PersonalInformation(StaticProperty):
        
    __tablename__ = "personalinformation"
    id: Mapped[int] = mapped_column(ForeignKey("staticproperty.id"), primary_key=True)
    address: Mapped[str] = mapped_column(String(100))
    name: Mapped[str] = mapped_column(String(100))
    gender: Mapped[str] = mapped_column(String(100))
    __mapper_args__ = {
        "polymorphic_identity": "personalinformation",
    }

class KnownLanguage(Base):
    
    __tablename__ = "knownlanguage"
    id: Mapped[int] = mapped_column(primary_key=True)
    level: Mapped[CEFR] = mapped_column(Enum(CEFR))
    name: Mapped[str] = mapped_column(String(100))


#--- Foreign keys and relationships of the nationality table
Nationality.personalinformation_id: Mapped["PersonalInformation"] = mapped_column(ForeignKey("personalinformation.id"), nullable=False)
Nationality.PersonalInformation: Mapped["PersonalInformation"] = relationship("PersonalInformation", back_populates="Nationality")

#--- Foreign keys and relationships of the interest table
Interest.personalinformation_id: Mapped["PersonalInformation"] = mapped_column(ForeignKey("personalinformation.id"), nullable=False)
Interest.PersonalInformation: Mapped["PersonalInformation"] = relationship("PersonalInformation", back_populates="Interest")

#--- Foreign keys and relationships of the user table
User.PersonalInformation: Mapped[List["PersonalInformation"]] = relationship("PersonalInformation", back_populates="User")

#--- Foreign keys and relationships of the age table
Age.personalinformation_id: Mapped["PersonalInformation"] = mapped_column(ForeignKey("personalinformation.id"), nullable=False)
Age.PersonalInformation: Mapped["PersonalInformation"] = relationship("PersonalInformation", back_populates="Age")

#--- Foreign keys and relationships of the hobby table
Hobby.personalinformation_id: Mapped["PersonalInformation"] = mapped_column(ForeignKey("personalinformation.id"), nullable=False)
Hobby.PersonalInformation: Mapped["PersonalInformation"] = relationship("PersonalInformation", back_populates="Hobby")

#--- Foreign keys and relationships of the personalinformation table
PersonalInformation.Hobby: Mapped[List["Hobby"]] = relationship("Hobby", back_populates="PersonalInformation")
PersonalInformation.Interest: Mapped[List["Interest"]] = relationship("Interest", back_populates="PersonalInformation")
PersonalInformation.Age: Mapped[List["Age"]] = relationship("Age", back_populates="PersonalInformation")
PersonalInformation.user_id: Mapped["User"] = mapped_column(ForeignKey("user.id"), nullable=False)
PersonalInformation.User: Mapped["User"] = relationship("User", back_populates="PersonalInformation")
PersonalInformation.Nationality: Mapped[List["Nationality"]] = relationship("Nationality", back_populates="PersonalInformation")
PersonalInformation.KnownLanguage: Mapped[List["KnownLanguage"]] = relationship("KnownLanguage", back_populates="PersonalInformation")

#--- Foreign keys and relationships of the knownlanguage table
KnownLanguage.personalinformation_id: Mapped["PersonalInformation"] = mapped_column(ForeignKey("personalinformation.id"), nullable=False)
KnownLanguage.PersonalInformation: Mapped["PersonalInformation"] = relationship("PersonalInformation", back_populates="KnownLanguage")