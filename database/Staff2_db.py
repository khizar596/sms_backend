from settings import sms_db
from fastapi import HTTPException
from bson import ObjectId
from models.Staff2 import Staff2, Staff2_modify
col_Staff2 = sms_db.Staff2
from database.Employee_db import col_employee, colr

from database.auth import AuthHandler

auth_handler=AuthHandler()



async def viewStaff2():
    employees=[]
    cursor = col_Staff2.find({'role.0.name':'staff'})

    for document in cursor:
        employees.append((Staff2(**document)))
    return employees

async def searchStaff2(employee_id : str)->dict:

    document=  col_employee.find_one({"_id": ObjectId(employee_id),'role.0.name':'staff'},{'_id':0})
    if not document:

        raise HTTPException(status_code=404, detail="Item not found")
    return document



async def addStaff2(details):
    employeedetails= details
    cursor = col_employee.find({})
    roles_relation=details['role']
    role_relation= [colr.find_one({"_id": ObjectId(roles_relation[0]),'role.0.name':'staff'},{'_id': 0})]

    for document in cursor:
        if document['cnic']==employeedetails['cnic']:
            response= {"CNIC " : "already exist "}
            return response
        elif document['email']==employeedetails['email']:
            response={"Email " : "already exist "}    
            return response
        elif not role_relation:
            raise HTTPException(status_code=404,detail="Please specify role")
    if role_relation:

        hashed = auth_handler.get_password_hash(employeedetails['password'])
        employeedetails['password']=hashed
        col_employee.insert_one(employeedetails) # Changing ki hab 
        return True
    else:
        return "Change your role kindly"

async def modifyStaff2(employee_id:str , details):
    if details['password']:
        hashed = auth_handler.get_password_hash(details['password'])
        details['password']=hashed
    roles_relation=details['role']
    role_relation= [colr.find_one({"_id": ObjectId(roles_relation[0])},{'_id': 0})]

    if role_relation!=None:
        details['role']=role_relation
    if details['role']:
        employe_role=details['role']
        role_relation= [colr.find_one({"_id": ObjectId(employe_role)},{'_id': 0})]
        details['role']=role_relation
    else : 
        return{"Please enter"}
    col_Staff2.update_one({"_id": ObjectId(employee_id)}, {"$set": details})
    return {"Succesfully updated the record"}

async def deleteStaff2id(employee_id:str):
    col_Staff2.delete_one({'_id': ObjectId(employee_id)})
    return True