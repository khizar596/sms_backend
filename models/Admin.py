from pydantic import BaseModel, Field
from typing import Optional



class Admin2(BaseModel):
   email:Optional[str]
   name : Optional[str] 
   password: Optional[str]
   role : str = Field(default='Admin')

   class Config:
        schema_extra = {
            "example": {
                               "email": "Admin@gmail.com",
                               "password":"admin123@1"                                           
                }}
        orm_mode = True
        allow_population_by_field_name = True
        arbitrary_types_allowed = True