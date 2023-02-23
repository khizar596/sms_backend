from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional, Union
from datetime import date 


class Emp_noticeboard(BaseModel):
    date : Union[str,date]
    description : str 
    Admin2id : str 
    HR2id : str
    class Config:
        schema_extra = {
            "example": {
                                "date" : date.today(),
                                "description" : "description",
                                "Admin2id" : "Admin2id",
                                "HR2id" : "hr2id",
                }}
        orm_mode = True
        allow_population_by_field_name = True
        arbitrary_types_allowed = True


class Emp_noticeboard_modify(BaseModel):
    date : Optional[Union[str,date]]
    description : Optional[str] 
    Admin2id : Optional[str] 
    HR2id : Optional[str]
    class Config:
        schema_extra = {
            "example": {
                                "date" : date.today(),
                                "description" : "description",
                                "Admin2id" : "Admin2id",
                                "HR2id" : "hr2id",
                }}
        orm_mode = True
        allow_population_by_field_name = True
        arbitrary_types_allowed = True