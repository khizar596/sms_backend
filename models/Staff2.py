from models.Employee2 import Employee2
from pydantic import Field

class Staff2(Employee2):
    Employee2id: int
    role : str = Field(default='Staff2')
