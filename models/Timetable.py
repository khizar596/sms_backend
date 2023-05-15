# from typing import Any, List, Union
from fastapi import FastAPI
from pydantic import BaseModel, Field
from typing import Optional, Union, List
from datetime import datetime, time


class Timetable(BaseModel):
    day  : int=Field (..., ge=1, le=31)
    start_time  : Union[str,datetime]
    end_time :   Union[str,datetime]
    Sectionid: str
    Class_subjectid: str
    Teacherid: str

    class Config:
        schema_extra ={
            "example": {
                            "day":3,
                            "start_time":datetime.now().time(),
                            "end_time":datetime.now().time(),
                            "Teacherid":"teacherid",

                            "Sectionid":"sectionid",
                            "Class_subjectid": "classsubjectid"
                            }
        }
        orm_mode = True
        allow_population_by_field_name = True
        arbitrary_types_allowed = True

class Timetable_modify(BaseModel):
    day  : Optional[int]
    start_time  : Optional[Union[str,datetime]]
    end_time :  Optional[Union[str,datetime]]
    Teacherid:  Optional[str]

    Sectionid: Optional[str]
    Class_subjectid: Optional[str]
    
    class Config:
        schema_extra ={
            "example": {
                            "day":4,
                            "start_time":datetime.now().time(),
                            "end_time":datetime.now().time(),
                            "Teacherid":"teacherid",
                            "Sectionid":"sectionid",
                            "Class_subjectid": "classsubjectid"
                            }
        }
        orm_mode = True
        allow_population_by_field_name = True
        arbitrary_types_allowed = True

        