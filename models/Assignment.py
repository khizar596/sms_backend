# from typing import Any, List, Union
from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional ,Union
from datetime import date 
app = FastAPI()

class Assignment(BaseModel):
    name: str
    date: Optional[Union[str, date]]
    total_marks: int
    obt_marks : int
    Class_subjectid: str
    class Config:
        schema_extra = {
            "example": {
                            "name" : "name",
                            "date" : date.today(),
                            "total_marks" : 25,
                            "obt_marks":20,
                            "Class_subjectid":"dfgh45asfvsdg436534fd",
                     
                        }
        }
            
        orm_mode = True
        allow_population_by_field_name = True
        arbitrary_types_allowed = True




        
class Assignment_modify(BaseModel):
    
    
    name: Optional[str]
    date: Optional[Union[str, date]]
    total_marks: Optional[int]
    obt_marks : Optional[int]
    Class_subjectid: Optional[str]
    class Config:
        schema_extra = {
            "example": {
                           "name" : "name",
                            "date" : date.today(),
                            "total_marks" : 25,
                            "obt_marks":20,
                            "Class_subjectid":"dfgh45asfvsdg436534fd",
                     
                        }
        }
            
        orm_mode = True
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
