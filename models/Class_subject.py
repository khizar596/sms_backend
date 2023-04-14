# from typing import Any, List, Union
from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional, List

app = FastAPI()


class Class_subject(BaseModel):
    Classid: str
    Courseid : str
    Teacherid: str
    class Config:
        schema_extra = {
            "example": {
                            "Classid" : "Classid",
                            "Courseid" :"Courseid",
                            "Teacherid" :"Teacherid",
            }
        }
        orm_mode = True
        allow_population_by_field_name = True
        arbitrary_types_allowed = True

class Class_subject_modify(BaseModel):
    Classid: Optional[str]
    Courseid : Optional[str]
    Teacherid: Optional[str]
    class Config:
        schema_extra = {
            "example": {
                            "Classid" : "Classid",
                            "Courseid" : "Courseid",
                            "Teacherid" : "Teacherid",
            }
        }
        orm_mode = True
        allow_population_by_field_name = True
        arbitrary_types_allowed = True

