from models.Employee2 import Employee2,Employee2_modify
from pydantic import Field 
from typing import List, Optional
class HR2(Employee2):
    # Employee2id: int
    role : List 
class HR2_modify(Employee2_modify):
    # Employee2id: int
    role : Optional[List] 