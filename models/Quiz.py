# from typing import Any, List, Union
from pydantic import BaseModel , Field
from typing import Optional , Union
from datetime import date , datetime 





class Quiz(BaseModel):
    name : str
    date : Union[str,date]
    start_time : datetime
    end_time : int  = Field( default= 10)
    total_marks : int 
    total_question : int
    Class_subjectid : str
    class Config:
        schema_extra = {
            "example": {
                            "name" : "str",
                            "date" : date.today(),
                            "start_time" : datetime.now(),
                            "end_time" : 23,
                            "total_marks" : 12,
                            "total_question":10,
                            "Class_subjectid" : 'str'
            }
        }
        orm_mode = True
        allow_population_by_field_name = True
        arbitrary_types_allowed = True


class Quiz_modify(BaseModel):
    name : Optional[str]
    date : Optional[Union[str,date]]
    start_time : Optional[Union[str, datetime]]
    end_time : Optional[int]
    total_marks : Optional[int] 
    total_question : Optional[int]
    Class_subjectid : Optional[str]
    class Config:
        schema_extra = {
            "example": {
                            "name" : "str",
                            "date" : date.today(),
                            "start_time" : datetime.now(),
                            "end_time" : 23,
                            "total_marks" : 12,
                            "total_question":10,
                            "Class_subjectid" : 'str'
            }
        }
        orm_mode = True
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
