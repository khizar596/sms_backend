# from typing import Any, List, Union
from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional



class Section(BaseModel):
    name : str 
    total_student: int
    Classid: str
    Sectionid: str
    class Config:
        schema_extra = {
            "example": {
                           "name" : "str" ,
                            "total_student": 23,
                            "Classid": "str" ,
                            "Sectionid": "str"
            }
        }
        orm_mode = True
        allow_population_by_field_name = True
        arbitrary_types_allowed = True


class Section_modify(BaseModel):
    name : Optional[str] 
    total_student: Optional[str]
    Classid: Optional[str]
    Sectionid: Optional[str]
    class Config:
        schema_extra = {
            "example": {
                           "name" : "str" ,
                            "total_student": 23,
                            "Classid": "str" ,
                            "Sectionid": "str"
            }
        }
        orm_mode = True
        allow_population_by_field_name = True
        arbitrary_types_allowed = True