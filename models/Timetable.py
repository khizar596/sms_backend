# from typing import Any, List, Union
from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional, Union
from datetime import datetime, time


class Timetable(BaseModel):
    day  : str
    start_time  : Union[str,datetime]
    end_time :  int
    Sectionid: str
    Class_subjectid: str
    
    class Config:
        schema_extra ={
            "example": {
                            "day":"Sunday",
                            "start_time":datetime.now(),
                            "end_time":23,
                            "Sectionid":"sectionid",
                            "Class_subjectid": "class subject id "
                            }
        }
        orm_mode = True
        allow_population_by_field_name = True
        arbitrary_types_allowed = True

class Timetable_modify(BaseModel):
    day  : Optional[str]
    start_time  : Optional[Union[str,datetime]]
    end_time :  Optional[int]
    Sectionid: Optional[str]
    Class_subjectid: Optional[str]
    
    class Config:
        schema_extra ={
            "example": {
                            "day":"Monday",
                            "start_time":datetime.now(),
                            "end_time":34,
                            "Sectionid":"sectionid",
                            "Class_subjectid": "class subject id "
                            }
        }
        orm_mode = True
        allow_population_by_field_name = True
        arbitrary_types_allowed = True

        