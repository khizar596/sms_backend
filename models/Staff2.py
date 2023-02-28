from models.Employee2 import Employee2,Employee2_modify
from pydantic import Field

class Staff2(Employee2):
    # Employee2id: int
    role : str = Field(default='Staff2')
class Staff2_modify(Employee2_modify):
    # Employee2id: int
    role : str = Field(default='Staff2')