from models.Employee2 import Employee2,Employee2_modify
from typing import Optional , List
class Staff2(Employee2):
    # Employee2id: int
    role : List = []
class Staff2_modify(Employee2_modify):
    # Employee2id: int
    role : Optional[List] = []
