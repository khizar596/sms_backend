# from typing import Any, List, Union
from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional



class EmployeeComplain(BaseModel):
   subject : str 
   description : str 
   Employee2id: str 
   HR2id : str 
   Admin2id : str
   class Config:
        schema_extra = {
            "example": {
                           "subject": "Title",
                            "description": "type subject",
                            "Employee2id": "23",
                            "HR2id": "42",
                            "Admin2id": "23",
                           
                            
                            
            }
        }
        orm_mode = True
        allow_population_by_field_name = True
        arbitrary_types_allowed = True


class EmployeeComplain_modify(BaseModel):
   subject : Optional[str] 
   description : Optional[str] 
   Employee2id: Optional[str] 
   HR2id : Optional[str] 
   Admin2id : Optional[str]
   class Config:
        schema_extra = {
            "example": {
                           "subject": "Title",
                            "description": "type subject",
                            "Employee2id": "Employee2's id ",
                            "HR2id": "HR2's id ",
                            "Admin2id": "Admin2id's id ",
                           
                            
                            
            }
        }
        orm_mode = True
        allow_population_by_field_name = True
        arbitrary_types_allowed = True

