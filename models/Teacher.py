from models.Employee2 import Employee2, Employee2_modify
from pydantic import Field
from typing import List,Optional
from datetime import date 
class Teacher(Employee2):
    # Employee2id: List=[]
    role : List 
   
class Teacher_modify(Employee2_modify):
    # Employee2id: List=[]
    role : Optional[List] 