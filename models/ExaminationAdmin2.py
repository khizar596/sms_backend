from models.Employee2 import Employee2_modify, Employee2
from typing import List,Optional
class ExaminationAdmin2(Employee2):
    role : List = []
class ExaminationAdmin2_modify(Employee2_modify):
    role : Optional[List] = []