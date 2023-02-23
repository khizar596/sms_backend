from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional , Union
from datetime import date


class Salary2(BaseModel):
    month: Union[str, date]
    status : bool = False
    amount : int
    total : int
    remaining : int 
    Employee2id : str
    Admin2id: str
    Accountant2id: str

class Salary2_modify(BaseModel):
    month: Optional[Union[str, date]]
    status : Optional[bool]
    amount : Optional[int]
    total : Optional[int]
    remaining : Optional[int] 
    Employee2id : Optional[str]
    Admin2id: Optional[str]
    Accountant2id: Optional[str]