from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional



class Class(BaseModel):
    class_name : str
    total_student: int
    class Config:
        schema_extra = {
            "example": {
                          "class_name":"Name likho yar",
                          "total_student":23,
          
            }
        }
        orm_mode = True
        allow_population_by_field_name = True
        arbitrary_types_allowed = True


class Class_modify(BaseModel):
    class_name : Optional[str]
    total_student: Optional[int]
    class Config:
        schema_extra = {
            "example": {
                          "class_name":"Name likho yar",
                          "total_student":23,
          
            }
        }
        orm_mode = True
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
