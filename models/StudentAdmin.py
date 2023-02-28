from models.Employee2 import Employee2,Employee2_modify
from pydantic import Field

class StudentAdmin(Employee2):
    role: str = Field(default='StudentAdmin')
class StudentAdmin_modify(Employee2_modify):
    role: str = Field( default =' StudentAdmin')