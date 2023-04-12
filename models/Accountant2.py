from models.Employee2 import Employee2
from pydantic import Field
from typing import List, Optional
class Accountant2(Employee2):
    role : List =[] 

class Accountant2_modify(Employee2):
    role : Optional[List] = []