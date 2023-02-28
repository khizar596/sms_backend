# from typing import Any, List, Union
from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional, List



class StudentComplain(BaseModel):
    subject: str
    description : str
    Studentid : List=[]
    Admin2id  : List=[]
    StudentAdminid : List=[]
    class Config:
        schema_extra = {
            "example": {
                           "subject": "Title",
                            "description": "type subject",
                            "Studentid": ["Student's id "],
                            "Admin2id": ["Admin2id's id "],
                            "StudentAdminid": ["StudentAdminid's id "]
                            
                            
            }
        }
        orm_mode = True
        allow_population_by_field_name = True
        arbitrary_types_allowed = True




# from typing import Any, List, Union
from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional



class StudentComplain_modify(BaseModel):
    subject: Optional['str']
    description : Optional['str']
    Studentid : Optional[List]
    Admin2id  : Optional[List]
    StudentAdminid : Optional[List]
    class Config:
        schema_extra = {
            "example": {
                            "subject": "Title",
                            "description": "type subject",
                            "Studentid": ["Student's id"],
                            "Admin2id": ["Admin2id's id "],
                            "StudentAdminid": ["StudentAdminid's id "]
                            
                            
            }
        }
        orm_mode = True
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
