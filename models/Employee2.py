# from typing import Any, List, Union
from fastapi import FastAPI ,UploadFile
from pydantic import BaseModel , EmailStr, Field
from typing import Optional , Union
from datetime import date 

app = FastAPI()


class Employee2(BaseModel):
    first_name: str
    last_name: str
    parent_name: str
    email  : EmailStr
    password: str
    address: str
    image: str#Optional[UploadFile] = Field(default=None,description="Image file as UploadFile")
    cnic: str
    reg_no : str
    dob: Union[str,date] 
    phone: int
    qualification: str
    salary : int
    bank_name : str
    account_name : int 
    title: str
    branch_code: str
    blood_group : str
    relegion : str
    role : str = Field(default='Employee')

    class Config:
        orm_mode = True
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        schema_extra = {
            "example": {
                "first_name": "str",
                                "last_name": "str",
                                "parent_name": "str",
                                "email"  : "Email@SMS.com",
                                "password": "str",
                                "address": "str",
                                "image": "str",
                                "cnic": "str",
                                "reg_no" : "str",
                                "dob": date.today() ,
                                "phone": 24,
                                "qualification": "str",
                                "salary" : 24,
                                "bank_name" : "str",
                                "account_name" : 24 ,
                                "title": "str",
                                "branch_code": "str",
                                "blood_group" : "str",
                                "relegion" : "str"
                            }
        }
class Employee2_modify(BaseModel):
    first_name: Optional[str]
    last_name: Optional[str]
    parent_name: Optional[str]
    email  : Optional[EmailStr]
    password: Optional[str]
    address: Optional[str]
    image: Optional[str]
    cnic: Optional[str]
    reg_no : Optional[str]
    dob: Optional[Union[str,date]] 
    phone: Optional[int]
    qualification: Optional[str]
    salary : Optional[int]
    bank_name : Optional[str]
    account_name : Optional[int] 
    title: Optional[str]
    branch_code: Optional[str]
    blood_group : Optional[str]
    relegion : Optional[str]
    class Config:
        orm_mode = True
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        schema_extra = {
            "example": {
                "first_name": "str",
                                "last_name": "str",
                                "parent_name": "str",
                                "email"  : "Email@SMS.com",
                                "password": "str",
                                "address": "str",
                                "image": "str",
                                "cnic": "str",
                                "reg_no" : "str",
                                "dob": date.today() ,
                                "phone": 23,
                                "qualification": "str",
                                "salary" : 23,
                                "bank_name" : "str",
                                "account_name" : 23 ,
                                "title": "str",
                                "branch_code": "str",
                                "blood_group" : "str",
                                "relegion" : "str"
                            }
        }
