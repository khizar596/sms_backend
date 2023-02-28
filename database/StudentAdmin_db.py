from settings import sms_db
from fastapi import HTTPException
from bson import ObjectId
from models.StudentAdmin import StudentAdmin, StudentAdmin_modify
col_StudentAdmin = sms_db.StudentAdmin
from database.Employee_db import col_employee

from database.auth import AuthHandler

auth_handler=AuthHandler()



async def viewStudentAdmin():
    employees=[]
    cursor = col_StudentAdmin.find({})

    for document in cursor:
        employees.append((StudentAdmin(**document)))
    return employees

async def searchStudentAdmin(employee_id : str)->dict:

    document=  col_StudentAdmin.find_one({"_id": ObjectId(employee_id)},{'_id': 0}) #ROLA WALA JAGA    
    # document=  col_employee.find_one({"_id": ObjectId(employee_id)}) #ROLA WALA JAGA
    
    if not document:

        raise HTTPException(status_code=404, detail="Item not found")
    
    return document


async def addStudentAdmin(details):
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
    col_StudentAdmin.insert_one(employeedetails) # Changing ki hab 
    return True

async def modifyStudentAdmin(employee_id:str , details):
    if details['password']:
        hashed = auth_handler.get_password_hash(details['password'])
        details['password']=hashed
    else : 
        return{"Please enter"}
    col_StudentAdmin.update_one({"_id": ObjectId(employee_id)}, {"$set": details})
    return {"Succesfully updated the record"}

async def deleteStudentAdminid(employee_id:str):
    col_StudentAdmin.delete_one({'_id': ObjectId(employee_id)})
    return True