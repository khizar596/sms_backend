# from typing import Any, List, Union
from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional, List



class StudentComplain(BaseModel):
    subject: str
    description : str
    Studentid : str
    Admin2id  : str
    StudentAdminid : str
    class Config:
        schema_extra = {
            "example": {
                           "subject": "Title",
                            "description": "type subject",
                            "Studentid": "Student's id ",
                            "Admin2id": "Admin2id's id ",
                            "StudentAdminid": "StudentAdminid's id "
                            
                            
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
    Studentid : Optional[str]
    Admin2id  : Optional[str]
    StudentAdminid : Optional[str]
    class Config:
        schema_extra = {
            "example": {
                            "subject": "Title",
                            "description": "type subject",
                            "Studentid": "Student's id",
                            "Admin2id": "Admin2id's id ",
                            "StudentAdminid": "StudentAdminid's id "
                            
                            
            }
        }
        orm_mode = True
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
  