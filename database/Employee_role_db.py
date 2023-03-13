from settings import sms_db
from fastapi import HTTPException
from bson import ObjectId
from models.Employee_role import EmployeeRole, Employeerole_modify, Role
col_Employee_role = sms_db.Employee_role
from database.Employee_db import col_employee

from database.auth import AuthHandler

auth_handler=AuthHandler()



async def viewEmployee_role():
    employees=[]
    cursor = col_Employee_role.find({})

    for document in cursor:
        employees.append((Role(**document)))
    return employees

async def searchEmployee_role(employee_id : str)->dict:

    document=  col_Employee_role.find_one({"_id": ObjectId(employee_id)},{'_id': 0}) #ROLA WALA JAGA    
    # document=  col_employee.find_one({"_id": ObjectId(employee_id)}) #ROLA WALA JAGA
    
    if not document:

        raise HTTPException(status_code=404, detail="Item not found")
    
    return document


async def addEmployee_role(details):
    employeedetails= details
    # cursor = col_employee.find({})
    # hashed = auth_handler.get_password_hash(employeedetails['password'])
    # employeedetails['password']=hashed
    col_Employee_role.insert_one(employeedetails) # Changing ki hab 
    return True

async def modifyEmployee_role(employee_id:str , details):
    col_Employee_role.update_one({"_id": ObjectId(employee_id)}, {"$set": details})
    return {"Succesfully updated the record"}

async def deleteEmployee_roleid(employee_id:str):
    col_Employee_role.delete_one({'_id': ObjectId(employee_id)})
    return True