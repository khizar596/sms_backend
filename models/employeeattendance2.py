
# from typing import Any, List, Union
from pydantic import BaseModel
from typing import Optional , Union
from datetime import date 


class employeeattendance2(BaseModel):
    date : Optional[Union[str,date]]
    type: str 
    Employee2id : str
    Admin2id : str 
    HR2id :str 
    class Config:
        schema_extra = {
            "example": {
                                "date" : date.today(),
                                "type" : "str",
                                "Employee2id" : 2,
                                "Admin2id" : 2 ,
                                "HR2id" :2 
                                                            
                }}
        orm_mode = True
        allow_population_by_field_name = True
        arbitrary_types_allowed = True



class employeeattendance2_modify(BaseModel):
    date : Optional[Union[str,date]]
    type: Optional[str] 
    Employee2id : Optional[int]
    Admin2id : Optional[int] 
    Hr2id :Optional[int] 
    class Config:
        schema_extra = {
            "example": {
                                "date" : date.today(),
                                "type" : "str",
                                "Employee2id" : 2,
                                "Admin2id" : 2 ,
                                "HR2id" :2 
                                                            
                }}
        orm_mode = True
        allow_population_by_field_name = True
        arbitrary_types_allowed = True