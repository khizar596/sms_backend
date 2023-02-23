# from typing import Any, List, Union
from fastapi import FastAPI
from pydantic import BaseModel , Field 
from typing import Optional
from datetime import datetime
app = FastAPI()


class Fee(BaseModel):
    admission: int
    monthly_fee: int
    scholarship: int
    discount: int
    status: bool = Field(default= 0)
    total_fee: int
    paid: int
    remaining: int
    fine: int
    date: Optional[datetime] = Field(default=datetime.utcnow())
    Studentid: str # description: Union[str, None] = None #Optional thing can be declared by none
    class Config:
        schema_extra = {
            "example": {
                            "admission": 1,
                            "monthly_fee": 1,
                            "schola0  rship": 1,
                            "discount": 1,
                            "status": 0,
                            "total_fee": 1,
                            "paid": 1,
                            "remaining": 1,
                            "fine": 3,
                            "date" : "2023-02-07T06:16:54.763Z",
                            "Studentid" : " 2"
            }
        }
        orm_mode = True
        allow_population_by_field_name = True
        arbitrary_types_allowed = True




        
class Fee_modify(BaseModel):
    admission:Optional[int]
    monthly_fee:Optional[int]
    scholarship:Optional[int]
    discount:Optional[int]
    status: Optional[bool]
    total_fee:Optional[int]
    paid:Optional[int]
    remaining:Optional[int]
    fine:Optional[int]
    date:Optional[int]
    class Config:
        schema_extra = {
            "example": {
                            "admission": 1,
                            "monthly_fee": 1,
                            "scholorship": 1,
                            "discount": 1,
                            "status": 1,
                            "total_fee": 1,
                            "paid": 1,
                            "remaining": 1,
                            "fine": 1,
                            "date" : "2023-02-07T06:16:54.763Z",
            }
        }
        orm_mode = True
        allow_population_by_field_name = True
        arbitrary_types_allowed = True