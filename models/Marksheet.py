# from typing import Any, List, Union
from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional



class Marksheet(BaseModel):
    total_marks : int
    obt_marks: int 
    grade : str
    comment : str 
    percentage: int
    Examid : int
    Student: int
    class Config:
        schema_extra ={
            "example": {
                            "total_marks" : 23,
                            "obt_marks": 23 ,
                            "grade" : "A",
                            "comment" : "Good" ,
                            "percentage": 23,
                            "Examid" : 23,
                            "Student": 23,
     }
        }
        orm_mode = True
        allow_population_by_field_name = True
        arbitrary_types_allowed = True




class Marksheet_modify(BaseModel):
    total_marks : Optional[int]
    obt_marks: Optional[int] 
    grade : Optional[str]
    comment : Optional[str] 
    percentage: Optional[int]
    Examid : Optional[int]
    Student: Optional[int]
    class Config:
        schema_extra ={
            "example": {
                            "total_marks" : 23,
                            "obt_marks": 23 ,
                            "grade" : "A",
                            "comment" : "Good" ,
                            "percentage": 23,
                            "Examid" : 23,
                            "Student": 23,
     }
        }
        orm_mode = True
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
