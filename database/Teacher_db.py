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
    cursor = col_employee.find({'role.0.name':'Teacher'})

    for document in cursor:
        document['_id']=str(document['_id'])

        employees.append((document))
    return employees

async def searchTeacher(employee_id : str)->dict:

    document=  col_employee.find_one({"_id": ObjectId(employee_id),'role.0.name':'Teacher'},{'_id':0})
    if not document:

        raise HTTPException(status_code=404, detail="Item not found")
    return document



async def addTeacher(details):
    employeedetails= details
    cursor = col_employee.find({})
    roles_relation=employeedetails['role']
    role_relation= [colr.find_one({"_id": ObjectId(roles_relation[0])},{'_id': 0})]
    if role_relation==[None]:
        raise HTTPException(405,"Role is not defined")
    for document in cursor:
        if document['cnic']==employeedetails['cnic']:
            response= {"CNIC " : "already exist "}
            return response
        elif document['email']==employeedetails['email']:
            response={"Email " : "already exist "}    
            return response
    hashed = auth_handler.get_password_hash(employeedetails['password'])
    employeedetails['password']=hashed
    employeedetails['role']=role_relation
    col_employee.insert_one(employeedetails) # Changing ki hab 
    return True

async def modifyTeacher(employee_id:str , details):
    if 'password' in details:
        if details['password']:
            hashed = auth_handler.get_password_hash(details['password'])
            details['password']=hashed
    if 'role' in details:
        if details['role']==[] :
            del details['role']

        else:

            try:
                employe_role=details['role'][0]
                role_relation= [colr.find_one({"_id": ObjectId(employe_role)},{'_id': 0})]
                details['role']=role_relation
            except:
                raise HTTPException(203, "define the role")
    col_employee.update_one({"_id": ObjectId(employee_id)}, {"$set": details})
    return {"Succesfully updated the record"}

async def deleteTeacherid(employee_id:str):
    col_employee.delete_one({'_id': ObjectId(employee_id)})
    return True