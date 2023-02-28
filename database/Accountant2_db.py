from settings import sms_db
from fastapi import HTTPException
from bson import ObjectId
from models.Accountant2 import Accountant2, Accountant2_modify
col_Accountant2 = sms_db.Accountant2
from database.Employee_db import col_employee

from database.auth import AuthHandler

auth_handler=AuthHandler()



async def viewAccountant2():
    employees=[]
    cursor = col_Accountant2.find({})

    for document in cursor:
        employees.append((Accountant2(**document)))
    return employees

async def searchAccountant2(employee_id : str)->dict:

    document=  col_Accountant2.find_one({"_id": ObjectId(employee_id)},{'_id': 0}) #ROLA WALA JAGA    
    # document=  col_employee.find_one({"_id": ObjectId(employee_id)}) #ROLA WALA JAGA
    
    if not document:

        raise HTTPException(status_code=404, detail="Item not found")
    
    return document


async def addAccountant2(details):
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
    col_Accountant2.insert_one(employeedetails) # Changing ki hab 
    return True

async def modifyAccountant2(employee_id:str , details):
    if details['password']:
        hashed = auth_handler.get_password_hash(details['password'])
        details['password']=hashed
    else : 
        return{"Please enter"}
    col_Accountant2.update_one({"_id": ObjectId(employee_id)}, {"$set": details})
    return {"Succesfully updated the record"}

async def deleteAccountant2id(employee_id:str):
    col_Accountant2.delete_one({'_id': ObjectId(employee_id)})
    return True