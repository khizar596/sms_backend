from settings import sms_db
from fastapi import HTTPException
from bson import ObjectId
from models.HR2 import HR2, HR2_modify
col_HR2 = sms_db.HR2
from database.Employee_db import col_employee

from database.auth import AuthHandler

auth_handler=AuthHandler()



async def viewHR2():
    employees=[]
    cursor = col_HR2.find({})

    for document in cursor:
        employees.append((HR2(**document)))
    return employees

async def searchHR2(employee_id : str)->dict:

    document=  col_HR2.find_one({"_id": ObjectId(employee_id)},{'_id': 0}) #ROLA WALA JAGA    
    # document=  col_employee.find_one({"_id": ObjectId(employee_id)}) #ROLA WALA JAGA
    
    if not document:

        raise HTTPException(status_code=404, detail="Item not found")
    
    return document


async def addHR2(details):
    employeedetails= details
    cursor = col_employee.find({})

    for document in cursor:
        if document['cnic']==employeedetails['cnic']:
            response= {"CNIC " : "already exist "}
            return response
        elif document['email']==employeedetails['email']:
            response={"Email " : "already exist "}    
            return response
    hashed = auth_handler.get_password_hash(employeedetails['password'])
    employeedetails['password']=hashed
    col_HR2.insert_one(employeedetails) # Changing ki hab 
    return True

async def modifyHR2(employee_id:str , details):
    if details['password']:
        hashed = auth_handler.get_password_hash(details['password'])
        details['password']=hashed
    else : 
        return{"Please enter"}
    col_HR2.update_one({"_id": ObjectId(employee_id)}, {"$set": details})
    return {"Succesfully updated the record"}

async def deleteHR2id(employee_id:str):
    col_HR2.delete_one({'_id': ObjectId(employee_id)})
    return True