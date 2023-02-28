from settings import sms_db
from fastapi import HTTPException
from bson import ObjectId
from models.ExaminationAdmin2 import ExaminationAdmin2, ExaminationAdmin2_modify
col_Examinationadmin = sms_db.Examinationadmin
from database.Employee_db import col_employee

from database.auth import AuthHandler

auth_handler=AuthHandler()



async def viewExaminationadmin():
    employees=[]
    cursor = col_Examinationadmin.find({})

    for document in cursor:
        employees.append((ExaminationAdmin2(**document)))
    return employees

async def searchExaminationadmin(employee_id : str)->dict:

    document=  col_Examinationadmin.find_one({"_id": ObjectId(employee_id)},{'_id': 0}) #ROLA WALA JAGA    
    # document=  col_employee.find_one({"_id": ObjectId(employee_id)}) #ROLA WALA JAGA
    
    if not document:

        raise HTTPException(status_code=404, detail="Item not found")
    
    return document


async def addExaminationadmin(details):
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
    col_Examinationadmin.insert_one(employeedetails) # Changing ki hab 
    return True

async def modifyExaminationadmin(employee_id:str , details):
    if details['password']:
        hashed = auth_handler.get_password_hash(details['password'])
        details['password']=hashed
    else : 
        return{"Please enter"}
    col_Examinationadmin.update_one({"_id": ObjectId(employee_id)}, {"$set": details})
    return {"Succesfully updated the record"}

async def deleteExaminationadminid(employee_id:str):
    col_Examinationadmin.delete_one({'_id': ObjectId(employee_id)})
    return True