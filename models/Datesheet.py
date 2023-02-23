
from pydantic import BaseModel
from typing import Optional, Union
from datetime import datetime, date


class Datesheet(BaseModel):
    day  : str
    start_time  : Union[str,datetime]
    end_time :  int
    date: Union[str,date]
    Sectionid: str
    Examid: str
    Class_subjectid: str
    
    class Config:
        schema_extra ={
            "example": {
                            "day":"Sunday",
                            "start_time":datetime.now(),
                            "end_time":23,
                            "date":date.today(),
                            "Sectionid":"sectionid",
                            "Examid":"Exam's id ",
                            "Class_subjectid" : "class subject id "
                            }
        }
        orm_mode = True
        allow_population_by_field_name = True
        arbitrary_types_allowed = True



class Datesheet_modify(BaseModel):
    day  : Optional[str]
    start_time  : Optional[Union[str,datetime]]
    end_time :  Optional[int]
    date: Optional[Union[str,date]]
    Sectionid: Optional[str]
    Examid: Optional[str]
    Class_subjectid: Optional[str]
    
    class Config:
        schema_extra ={
            "example": {
                            "day":"Sunday",
                            "start_time":datetime.now(),
                            "end_time":43,
                            "date":date.today(),
                            "Sectionid":"sectionid",
                            "Examid":"Exam's id ",
                            "Class_subjectid" : "class subject id "
                            }
        }
        orm_mode = True
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
