from models.Employee2 import Employee2
from settings import sms_db
from fastapi import HTTPException
from bson import ObjectId
from database.auth import AuthHandler, colr
auth_handler=AuthHandler()
col_employee = sms_db.Employees




async def viewemployee():
    employees=[]
    cursor = col_employee.find({})

    for document in cursor:
        document['_id']=str(document['_id'])

        employees.append(document)
    return employees

async def searchemployee(employee_id : str)->dict:

    document=  col_employee.find_one({"_id": ObjectId(employee_id)},{'_id': 0}) #ROLA WALA JAGA    
    # document=  col_employee.find_one({"_id": ObjectId(employee_id)}) #ROLA WALA JAGA
    
    if not document:

        raise HTTPException(status_code=404, detail="Item not found")
    
    return document


async def enrollemployee(details):
    employeedetails= details
    cursor = col_employee.find({})
    roles_relation=employeedetails['role']
    role_relation= [colr.find_one({"_id": ObjectId(roles_relation[0])},{'_id': 0})]

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

async def modifyemployee(employee_id:str , details):
    
    if  "role" in details:
        roles_relation=details['role']
        role_relation= [colr.find_one({"_id": ObjectId(roles_relation[0])},{'_id': 0})] 
    
        if role_relation==None:
            del details['role']
    
    if  "password" in details:
        hashed = auth_handler.get_password_hash(details['password'])
        details['password']=hashed
    
    col_employee.update_one({"_id": ObjectId(employee_id)}, {"$set": details})
    return {"Succesfully updated the record"}

async def deletebyid(employee_id:str):
    col_employee.delete_one({'_id': ObjectId(employee_id)})
    return True
