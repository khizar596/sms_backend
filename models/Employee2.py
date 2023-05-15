# from typing import Any, List, Union
from fastapi import FastAPI ,UploadFile
from pydantic import BaseModel , EmailStr, Field
from typing import Optional , Union , List
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
    account_number : int 
    title: str
    branch_code: str
    blood_group : str
    relegion : str
    role : List =[]

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
                                "account_number" : 24 ,
                                "title": "str",
                                "branch_code": "str",
                                "blood_group" : "str",
                                "relegion" : "str",
                                "role" : ["employeerole"]
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
    account_number : Optional[int] 
    title: Optional[str]
    branch_code: Optional[str]
    blood_group : Optional[str]
    relegion : Optional[str]
    role : Optional[List] =[]

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
                                "bank_number" : "str",
                                "account_name" : 23 ,
                                "title": "str",
                                "branch_code": "str",
                                "blood_group" : "str",
                                "relegion" : "str",
                                "role" : ["employeerole"]
                            }
        }
