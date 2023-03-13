# from typing import Any, List, Union
from pydantic import BaseModel , Field
from typing import Optional,List
from models.Employee2 import Employee2_modify,Employee2




class EmployeeRole(Employee2):
    name : str 
    status: bool = Field(default=False)
    
    class Config:
        orm_mode = True
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
class Role(BaseModel):
    name : str 
    status: bool = Field(default=False)

    class Config:
        orm_mode = True
        allow_population_by_field_name = True
        arbitrary_types_allowed = True

class Employeerole_modify(Employee2_modify):
    name : Optional[str]
    status: Optional[bool] = Field(default=False)
  
    class Config:
        orm_mode = True
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
