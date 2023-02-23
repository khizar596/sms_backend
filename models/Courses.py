from pydantic import BaseModel
from typing import Optional


class Courses(BaseModel):
    name : str
    class Config:
        schema_extra = {
            "example": {
                                "name" : "name"
                }}
        orm_mode = True
        allow_population_by_field_name = True
        arbitrary_types_allowed = True

class Courses_modify(BaseModel):
    name : Optional[str]
    class Config:
        schema_extra = {
            "example": {
                            "name" : "name"
            }}
        orm_mode = True
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
