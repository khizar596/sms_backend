from fastapi import FastAPI
from pydantic import BaseModel , Field, EmailStr
app = FastAPI()


class AuthDetails(BaseModel):
    email : EmailStr 
    password : str = Field(min_length=8,description='Password must contains Special character') 
    
    class Config:
        schema_extra = {
            "example": {
                            "email":"khansa@gmail.com",
                            "password" : "password@123"
            }
        }
        orm_mode = True
        allow_population_by_field_name = True
        arbitrary_types_allowed = True

