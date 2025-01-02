from datetime import datetime, date
from typing import List, Optional, Union, Set
from enum import Enum
from pydantic import BaseModel

from abc import ABC, abstractmethod

############################################
# Enumerations are defined here
############################################

class CEFR(Enum):
    A2 = "A2"
    C2 = "C2"
    B1 = "B1"
    A1 = "A1"
    B2 = "B2"
    C1 = "C1"

############################################
# Classes are defined here
############################################
class Nationality(BaseModel):
    name: str
    id: int  # id created
    personalinformation_id: int  # N:1 Relationship

class StaticProperty(ABC, BaseModel):
    id: int  # id created
    pass

class PersonalInformation(StaticProperty):
    address: str
    gender: str
    name: str
    id: int  # id created
    user_id: int  # N:1 Relationship

class Hobby(BaseModel):
    name: str
    id: int  # id created

class User(BaseModel):
    name: str
    id: int  # id created

class Age(BaseModel):
    value: int
    id: int  # id created

class Interest(BaseModel):
    name: str
    id: int  # id created

class KnownLanguage(BaseModel):
    level: CEFR
    name: str
    id: int  # id created

