from fastapi import FastAPI
from pydantic import BaseModel , Field, EmailStr 
from typing import Optional , Union , List

from models.Employee2 import Employee2_modify,Employee2
app = FastAPI()


class AuthDetails(BaseModel):
    email : EmailStr 
    password : str = Field(...) 
    
    class Config:
        schema_extra = {
            "example": {
                            "email": "admin@gmail.com",
                            "password": "password@123"
}
        }
        orm_mode = True
        allow_population_by_field_name = True
        arbitrary_types_allowed = True

class registration2(Employee2):
    role:List=[]
    status:bool = Field(default=False) 
    
    class Config:
        orm_mode = True
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
