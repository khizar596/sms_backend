from models.Employee2 import Employee2,Employee2_modify
from pydantic import Field 
from typing import List
class HR2(Employee2):
    # Employee2id: int
    role : List = Field(default='HR2')
class HR2_modify(Employee2_modify):
    # Employee2id: int
    role : List = Field(default='HR2')