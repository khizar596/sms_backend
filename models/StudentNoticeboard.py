# from typing import Any, List, Union
from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional,Union
from datetime import date 


class StudentNoticeboard(BaseModel):
   date : Union[str,date]
   description : str 
   Admin2id : str 
   StudentAdminid : str
   class Config:
        schema_extra = {
            "example": {
                            "date":date.today(),
                            "description":"description",
                            "Admin2id":"Admin2id",
                            "StudentAdminid":"StudentAdminid",

            }
        }
        orm_mode = True
        allow_population_by_field_name = True
        arbitrary_types_allowed = True

class StudentNoticeboard_modify(BaseModel):
   date : Optional[Union[str,date]]
   description : Optional[str] 
   Admin2id : Optional[str] 
   StudentAdminid : Optional[str]
   class Config:
        schema_extra = {
            "example": {
                            "date":date.today(),
                            "description":"description",
                            "Admin2id":"Admin2id",
                            "StudentAdminid":"StudentAdminid",

            }
        }
        orm_mode = True
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
