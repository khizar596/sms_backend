# from typing import Any, List, Union
from fastapi import FastAPI
from pydantic import BaseModel, Field 
from typing import Optional, List
from datetime import datetime , date 

app = FastAPI()
class Chatbox(BaseModel):
    description: str
    Time: Optional[datetime] 
    Date: Optional[date]= date.today()
    Studentid : List = []
    Class_subjectid: List = []
    Teacherid: List = []
    Admin2id: List = []
    StudentAdminid: List = []
 # description: Union[List = [], None] = None s#Optional thing can be declared by none
  
    class Config:
        schema_extra ={
            "example": {
                            "description":"description",
                            "Time" :datetime.now().time(),
                            "Date" : date.today(),
                            "Studentid":"description",
                            "Class_subjectid" : ["1234"],
                            "Teacherid":["Teacherid"],
                            "Admin2id":["Admin2id"],
                            "StudentAdminid":["Studentadminid"]
                            }
        }
        orm_mode = True
        allow_population_by_field_name = True
        arbitrary_types_allowed = True


class Chatbox_modify(BaseModel):
    description: Optional[str]
    Time: Optional[datetime]
    Date: Optional[datetime] 
    Studentid : Optional[List]
    Class_subjectid: Optional[List]
    Teacherid: Optional[List]
    Admin2id: Optional[List]
    StudentAdminid: Optional[List]
 # description: Union[str, None] = None #Optional thing can be declared by none
  
    class Config:
        schema_extra = {
            "example":  {
                            "description":"description",
                            "Time" :datetime.now().time(),
                            "Date" : date.today(),
                            "Studentid":["studentidn"],
                            "CLass_subjectid":["CLass_subjectid"],
                            "Teacherid":["Teacherid"],
                            "Admin2id":["Admin2id"],
                            "StudentAdminid":["Studentadminid"]
                            }}
        orm_mode = True
        allow_population_by_field_name = True
        arbitrary_types_allowed = True