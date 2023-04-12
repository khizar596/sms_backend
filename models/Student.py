from pydantic import BaseModel , EmailStr ,Field
from typing import Optional, Union, List
from datetime import date
from bson import ObjectId
class Student(BaseModel):

    first_name: str
    last_name: str
    parent_name: str
    password: str
    cnic: str
    address: str
    gender: str
    dob: Union[str,date] = date.today()
    email: EmailStr
    image: str
    phone: int
    blood_group: str
    religion: str
    previous_school: str
    session: str
    class_id : str #List = [ ]
    # parentid:str #List = [ ]
    blocked: Optional[bool]  = Field(default=False)
    role : List = []
    # description: Union[str, None] = None #Optional thing can be declared by none

    class Config:
        orm_mode = True
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        schema_extra = {
            "example": {
                            "first_name": "str",
                            "last_name": "str",
                            "parent_name": "str", 
                            "password": "str",
                            "cnic": "str",
                            "address": "str",
                            "gender": "str",
                            "dob": date.today(),
                            "email": "str",
                            "image": "str",
                            "phone": 12,
                            "blood_group": "str",
                            "religion": "str",
                            "previous_school": "str",
                            "session": "str",
                            "class_id" : "12",
                            # "parentid": ["12"],
                            "role":["6408253889ef7f7b8105f2d9"]
            }
        }


class Student_modify(BaseModel):
    first_name: Optional[str]
    last_name: Optional[str]
    parent_name: Optional[str]
    password: Optional[str]
    cnic: Optional[str]
    address: Optional[str]
    gender: Optional[str]
    dob: Optional[Union[str,date]]   #  "dob": "2023-02-07T06:16:54.763Z"
    email: Optional[EmailStr]
    image: Optional[str]
    phone: Optional[int]
    blood_group: Optional[str]
    religion: Optional[str]
    previous_school: Optional[str]
    session: Optional[str]
    class_id : Optional[str] 
    # parentid:Optional[str] 
    blocked: Optional[bool]
    role : Optional[List] 

    # description: Union[str, None] = None #Optional thing can be declared by none
    
    class Config:
        orm_mode = True
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        # json_encoders = {ObjectId: str}