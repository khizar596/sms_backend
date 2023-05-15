# from typing import Any, List, Union
from pydantic import BaseModel
from typing import Optional , Union, List
from datetime import date 


class StudentAttendence(BaseModel):
    date: Union[str,date]
    type : str
    Studentid: str
    class Config:
        schema_extra = {
            "example": {
                                "date" : date.today(),
                                "type" : "str",
                                "Studentid" : "2",
                                
                                                            
                }}
        orm_mode = True
        allow_population_by_field_name = True
        arbitrary_types_allowed = True

    
class StudentAttendence_modify(BaseModel):
    date: Optional[Union[str,date]]
    type : Optional[str]
    Studentid: Optional[str]
    class Config:
        schema_extra = {
            "example": {
                                "date" : date.today(),
                                "type" : "D",
                                "Studentid" : "2",
                                
                                                            
                }}
        orm_mode = True
        allow_population_by_field_name = True
        arbitrary_types_allowed = True