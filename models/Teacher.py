from models.Employee2 import Employee2
from pydantic import Field


class Teacher(Employee2):
    Employee2id: int
    role : str = Field(default='Teacher')
