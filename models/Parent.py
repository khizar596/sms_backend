from pydantic import BaseModel , EmailStr ,Field
from typing import Optional
from datetime import datetime


class Parent(BaseModel):
    name: str
    password: str
    cnic: str
    address: str
    gender: str
    dob: Optional[datetime] = datetime.now() #  "dob": "2023-02-07T06:16:54.763Z"
    email: EmailStr
    image: str
    phone: int
    profession: str # description: Union[str, None] = None #Optional thing can be declared by none
    role : str = Field(default='Parent')

    class Config:
        schema_extra = {
            "example": {
                            "name": "str",
                            "password": "str",
                            "cnic": "str",
                            "address": "str",
                            "gender": "str",
                            "dob": "int",
                            "email": "str",
                            "image": "str",
                            "phone": "int",
                            "profession" : " str"
            }
        }
        orm_mode = True
        allow_population_by_field_name = True
        arbitrary_types_allowed = True


    
class Parent_modify(BaseModel):
    name: Optional[str]
    password: Optional[str]
    cnic: Optional[str]
    address: Optional[str]
    gender: Optional[str]
    dob: Optional[datetime] = datetime.now() #  "dob": "2023-02-07T06:16:54.763Z"
    email: Optional[str]
    image: Optional[str]
    phone: Optional[int]
    profession: Optional[str] # description: Union[Optional[str], None] = None #Optional thing can be declared by none
    class Config:
        schema_extra = {
            "example": {
                            "name": "Optional[str]",
                            "password": "Optional[str]",
                            "cnic": "Optional[str]",
                            "address": "Optional[str]",
                            "gender": "Optional[str]",
                            "dob": "int",
                            "email": "Optional[str]",
                            "image": "Optional[str]",
                            "phone": "int",
                            "profession" : " Optional[str]"
            }
        }
        orm_mode = True
        allow_population_by_field_name = True
        arbitrary_types_allowed = True