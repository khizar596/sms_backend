from settings import sms_db
from fastapi import HTTPException
from bson import ObjectId
from models.Teacher import Teacher, Teacher_modify
col_Teacher = sms_db.Teacher
from database.Employee_db import col_employee, colr

from database.auth import AuthHandler

auth_handler=AuthHandler()



async def viewTeacher():
    employees=[]
    cursor = col_Teacher.find({'role.0.name':'Teacher'})

    for document in cursor:
        employees.append((Teacher(**document)))
    return employees

async def searchTeacher(employee_id : str)->dict:

    document=  col_employee.find_one({"_id": ObjectId(employee_id),'role.0.name':'Teacher'},{'_id':0})
    if not document:

        raise HTTPException(status_code=404, detail="Item not found")
    return document



async def addTeacher(details):
    employeedetails= details
    cursor = col_employee.find({})
    employe_role=employeedetails['role']
    role_relation= [colr.find_one({"_id": ObjectId(employe_role[0])},{'_id': 0,'name':1})]

    for document in cursor:
        if document['cnic']==employeedetails['cnic']:
            response= {"CNIC " : "already exist "}
            return response
        elif document['email']==employeedetails['email']:
            response={"Email " : "already exist "}    
            return response
        elif not role_relation:
            raise HTTPException(status_code=404,detail="Please specify role")
    if role_relation=="Teacher":
        employeedetails['role']=role_relation

        hashed = auth_handler.get_password_hash(employeedetails['password'])
        employeedetails['password']=hashed
        col_employee.insert_one(employeedetails) # Changing ki hab 
        return True
    else:
        return "Change your role kindly"

async def modifyTeacher(employee_id:str , details):
    if details['password']:
        hashed = auth_handler.get_password_hash(details['password'])
        details['password']=hashed
    if details['role']:
        employe_role=details['role']
        role_relation= [colr.find_one({"_id": ObjectId(employe_role)},{'_id': 0})]

        details['role']=role_relation
    else : 
        return{"Please enter"}
    col_Teacher.update_one({"_id": ObjectId(employee_id)}, {"$set": details})
    return {"Succesfully updated the record"}

async def deleteTeacherid(employee_id:str):
    col_Teacher.delete_one({'_id': ObjectId(employee_id)})
    return True