from settings import sms_db
from fastapi import HTTPException
from bson import ObjectId
from models.employeeattendance2 import employeeattendance2
col_Emp_Attendence2 = sms_db.Emp_Attendence2



async def viewEmp_Attendence2():
    Emp_Attendence2s=[]
    cursor = col_Emp_Attendence2.find({})

    for document in cursor:
        Emp_Attendence2s.append((employeeattendance2(**document)))
    return Emp_Attendence2s

async def searchEmp_Attendence2(Emp_Attendence2_id : str)->dict:

    document=  col_Emp_Attendence2.find_one({"_id": ObjectId(Emp_Attendence2_id)},{'_id': 0}) 
    
    if not document:

        raise HTTPException(status_code=404, detail="document not found")
    
    return document


async def addEmp_Attendence2(details):
    Emp_Attendence2details= details
    
    col_Emp_Attendence2.insert_one(Emp_Attendence2details) # Changing ki hab 
    return True

async def modifyEmp_Attendence2(Emp_Attendence2_id:str , details):
    col_Emp_Attendence2.update_one({"_id": ObjectId(Emp_Attendence2_id)}, {"$set": details})
    return {"Succesfully updated the record"}

async def deleteEmp_Attendence2id(Emp_Attendence2_id:str):
    col_Emp_Attendence2.delete_one({'_id': ObjectId(Emp_Attendence2_id)})
    return True
