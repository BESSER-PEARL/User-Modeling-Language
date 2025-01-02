from datetime import datetime, date
from typing import List, Optional, Union,Set
from pydantic import BaseModel

############################################
#
# The classes are defined here
#
############################################

from abc import ABC, abstractmethod
            


class KnownLanguageCreate(BaseModel):
    level: CEFR
    name: str

            

 
@startuml

class KnownLanguage {
name: str
level: CEFR
}



enum CEFR {
A1
A2
B1
B2
C1
C2
}




@enduml
