# from typing import Any, List, Union
from fastapi import FastAPI
from pydantic import BaseModel, Field 
from typing import Optional, List,Union
from datetime import datetime , date 

app = FastAPI()
class Chatbox(BaseModel):
    description: str
    Time: Union[str,datetime] 
    Date: Union[str,date]= date.today()
    Studentid : str
    Class_subjectid: str
    Teacherid: str
    Admin2id: str
    StudentAdminid: str
 # description: Union[List, None] = None s#Optional thing can be declared by none
  
    class Config:
        schema_extra ={
            "example": {
                            "description":"description",
                            "Time" :datetime.now().time(),
                            "Date" : date.today(),
                            "Studentid":"studentid",
                            "Class_subjectid" : "1234",
                            "Teacherid":"Teacherid",
                            "Admin2id":"Admin2id",
                            "StudentAdminid":"Studentadminid"
                            }
        }
        orm_mode = True
        allow_population_by_field_name = True
        arbitrary_types_allowed = True


class Chatbox_modify(BaseModel):
    description: Optional[str]
    Time: Optional[datetime]
    Date: Optional[datetime] 
    Studentid : Optional[str]
    Class_subjectid: Optional[str]
    Teacherid: Optional[str]
    Admin2id: Optional[str]
    StudentAdminid: Optional[str]
 # description: Union[str, None] = None #Optional thing can be declared by none
  
    class Config:
        schema_extra = {
            "example":  {
                            "description":"description",
                            "Time" :datetime.now().time(),
                            "Date" : date.today(),
                            "Studentid":"studentid",
                            "Class_subjectid" : "1234",
                            "Teacherid":"Teacherid",
                            "Admin2id":"Admin2id",
                            "StudentAdminid":"Studentadminid"
                            }}
        orm_mode = True
        allow_population_by_field_name = True
        arbitrary_types_allowed = True