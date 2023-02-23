# from typing import Any, List, Union
from fastapi import FastAPI
from pydantic import BaseModel , Field
from typing import Optional
from datetime import datetime
app = FastAPI()


class Question(BaseModel):
    question : str 
    option : str 
    answer : str 
    timer : int
    obt_marks : int 
    Quizz_id : str
    class Config:
        schema_extra = {
            "example": {
                            "question" : "str",
                            "option" : "str",
                            "answer" : "str",
                            "timer" : 231,
                            "obt_marks" : 12,
                            "Quizz_id" : "str",
            }
        }
        orm_mode = True
        allow_population_by_field_name = True
        arbitrary_types_allowed = True


class Question_modify(BaseModel):
    question : Optional[str] 
    option : Optional[str] 
    answer : Optional[str] 
    timer : Optional[int] =  Field (default=10)
    obt_marks : Optional[int] 
    Quizz_id : Optional[str]
    class Config:
        schema_extra = {
            "example": {
                            "question" : "str",
                            "option" : "str",
                            "answer" : "str",
                            "timer" : 10,
                            "obt_marks" : 12,
                            "Quizz_id" : "str",
            }
        }
        orm_mode = True
        allow_population_by_field_name = True
        arbitrary_types_allowed = True