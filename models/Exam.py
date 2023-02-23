# from typing import Any, List, Union
from pydantic import BaseModel
from typing import Optional ,Union
from datetime import date

class Exam(BaseModel):
    name: str
    year: Optional[Union[str,date]]
    class Config:
        schema_extra = {
            "example": {
                                "name" : "name",
                                "year" : date.today().year
                }}
        orm_mode = True
        allow_population_by_field_name = True
        arbitrary_types_allowed = True


class Exam_modify(BaseModel):
    name: Optional[str]
    year: Optional[Union[str,date]]
    class Config:
        schema_extra = {
            "example": {
                                "name" : "name_modify",
                                "year" : date.today().year
                }}
        orm_mode = True
        allow_population_by_field_name = True
        arbitrary_types_allowed = True