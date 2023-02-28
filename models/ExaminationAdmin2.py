from models.Employee2 import Employee2_modify, Employee2
from pydantic import Field

class ExaminationAdmin2(Employee2):
    role : str = Field(default='Examination_Admin')
class ExaminationAdmin2_modify(Employee2_modify):
    role : str = Field(default='Examination_Admin')