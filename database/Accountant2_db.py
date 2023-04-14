from settings import sms_db
from fastapi import HTTPException
from bson import ObjectId
from models.Accountant2 import Accountant2, Accountant2_modify
col_Accountant2 = sms_db.Accountant2
from database.Employee_db import col_employee, colr

from database.auth import AuthHandler

auth_handler=AuthHandler()



async def viewAccountant2():
    employees=[]
    cursor = col_employee.find({'role.0.name':'Accountant'})

    for document in cursor:
        document['_id']=str(document['_id'])
        employees.append(document)
    return employees

async def searchAccountant2(employee_id : str)->dict:

    document=  col_employee.find_one({"_id": ObjectId(employee_id),'role.0.name':'Accountant'},{'_id':0})
    if not document:

        raise HTTPException(status_code=404, detail="Item not found")
    return document


async def addAccountant2(details):
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
    if role_relation=="Accountant":
        employeedetails['role']=role_relation

        hashed = auth_handler.get_password_hash(employeedetails['password'])
        employeedetails['password']=hashed
        col_employee.insert_one(employeedetails) # Changing ki hab 
        return True
    else:
        return "Change your role kindly"

async def modifyAccountant2(employee_id:str , details):
    if details['role']==[]:
        del details['role']
    try:
        if details['password']:
            hashed = auth_handler.get_password_hash(details['password'])
            details['password']=hashed
    
    except:
        pass
    if details['role']:
        try:
            employe_role=details['role'][0]
            role_relation= [colr.find_one({"_id": ObjectId(employe_role)},{'_id': 0})]
            details['role']=role_relation
        except:
            raise HTTPException(203)
    col_employee.update_one({"_id": ObjectId(employee_id)}, {"$set": details})
    return {"Succesfully updated the record"}

async def deleteAccountant2id(employee_id:str):
    col_employee.delete_one({'_id': ObjectId(employee_id)})
    return True