from datetime import datetime, date
from typing import List, Optional, Union, Set
from enum import Enum
from pydantic import BaseModel

from abc import ABC, abstractmethod

############################################
# Enumerations are defined here
############################################

class CEFR(Enum):
    B2 = "B2"
    C1 = "C1"
    A2 = "A2"
    C2 = "C2"
    A1 = "A1"
    B1 = "B1"

############################################
# Classes are defined here
############################################
class KnownLanguageCreate(BaseModel):
    level: CEFR
    name: str
    personalinformation_id: int  # N:1 Relationship

class StaticPropertyCreate(ABC, BaseModel):
    pass

class PersonalInformationCreate(StaticPropertyCreate):
    address: str
    name: str
    gender: str
    user_id: int  # N:1 Relationship

class HobbyCreate(BaseModel):
    name: str
    personalinformation_id: int  # N:1 Relationship

class AgeCreate(BaseModel):
    value: int
    personalinformation_id: int  # N:1 Relationship

class UserCreate(BaseModel):
    name: str

class InterestCreate(BaseModel):
    name: str
    personalinformation_id: int  # N:1 Relationship

class NationalityCreate(BaseModel):
    name: str
    personalinformation_id: int  # N:1 Relationship

