from models.Employee2 import Employee2
from pydantic import Field

class Accountant2(Employee2):
    role : str = Field(default='Accountant2')

class Accountant2_modify(Employee2):
    role : str = Field(default='Accountant2')