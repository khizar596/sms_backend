from pydantic import BaseModel, Field
from typing import Optional,List



class Admin2(BaseModel):
   email:Optional[str]
   name : Optional[str] 
   password: Optional[str]
   role : List =[]

   class Config:
        schema_extra = {
            "example": {
                               "email": "Admin@gmail.com",
                               "password":"admin123@1" ,
                               "role":["64082dad89ef7f7b8105f2db"]                                          
                }}
        orm_mode = True
        allow_population_by_field_name = True
        arbitrary_types_allowed = True