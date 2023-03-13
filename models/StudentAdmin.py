from models.Employee2 import Employee2,Employee2_modify
from typing import List, Optional
class StudentAdmin(Employee2):
    role: List = []
class StudentAdmin_modify(Employee2_modify):
    role: Optional[List] = []