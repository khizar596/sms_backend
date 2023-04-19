from settings import sms_db
from bson import ObjectId
from fastapi import HTTPException
from database.Employee_db import col_employee as cole
from database.Admin_db import col_Admin 
from models.EmployeeNoticeboard2 import Emp_noticeboard
col_empnotice = sms_db.Emp_Noticeboard



async def viewempnotice():
    empnotices=[]
    cursor = col_empnotice.find({})

    for document in cursor:
        HR_relation = cole.find_one({"_id": ObjectId(document['Hr2id']), 'role.0.name': 'HR'}, {'_id': 0,'first_name':1})
        Admin2id_relation = col_Admin.find_one({"_id": ObjectId(document['Admin2id']), 'role.0.name': 'Admin'}, {'_id': 0,'name':1})
        if not None and HR_relation and Admin2id_relation:
            document['_id']=str(document['_id'])
            document['Hr2id'] = HR_relation
            document['Admin2id'] = Admin2id_relation
        document['_id']=str(document['_id'])

        empnotices.append(document)
    return empnotices

async def searchempnotice(empnotice_id : str)->dict:

    document=  col_empnotice.find_one({"_id": ObjectId(empnotice_id)},{'_id': 0}) 
    
    if not document:

        raise HTTPException(status_code=404, detail="document not found")
    HR_relation = cole.find_one({"_id": ObjectId(document['Hr2id']), 'role.0.name': 'HR'}, {'_id': 0,'first_name':1})
    Admin2id_relation = col_Admin.find_one({"_id": ObjectId(document['Admin2id']), 'role.0.name': 'Admin'}, {'_id': 0,'name':1})
    if not None and HR_relation and Admin2id_relation:
        document['_id']=str(document['_id'])
        document['Hr2id'] = HR_relation
        document['Admin2id'] = Admin2id_relation
    return document


async def addempnotice(details):
    if  "Employee2id" in details:
        Employee2id_relation = cole.find_one({"_id": ObjectId(details['Employee2id'])}, {'_id': 0,'first_name':1})
        if Employee2id_relation==None:
            raise HTTPException(204, detail="check your Employee id")
    if "Hr2id" in details:
        HR_relation = cole.find_one({"_id": ObjectId(details['Hr2id']), 'role.0.name': 'HR'}, {'_id': 0,'first_name':1})
        if HR_relation==None:
            raise HTTPException(204, detail="check your HR id")
    if "Admin2id" in details:
        Admin2id_relation = col_Admin.find_one({"_id": ObjectId(details['Admin2id']), 'role.0.name': 'Admin'}, {'_id': 0,'name':1})
        
        if Admin2id_relation==None:
            raise HTTPException(204, detail="check your Admin id")
    col_empnotice.insert_one(details) 
    return True

async def modifyempnotice(empnotice_id:str , details):
    if  "Employee2id" in details:
        Employee2id_relation = cole.find_one({"_id": ObjectId(details['Employee2id'])}, {'_id': 0,'first_name':1})

        if Employee2id_relation==None:
            del details['Employee2id']
    if "Hr2id" in details:
        HR_relation = cole.find_one({"_id": ObjectId(details['Hr2id']), 'role.0.name': 'HR'}, {'_id': 0,'first_name':1})
        if HR_relation==None:
            del details['Hr2id']
    if "Admin2id" in details:
        Admin2id_relation = col_Admin.find_one({"_id": ObjectId(details['Admin2id']), 'role.0.name': 'Admin'}, {'_id': 0,'name':1})
        
        if Admin2id_relation==None:
            del details['Admin2id']
    
    col_empnotice.update_one({"_id": ObjectId(empnotice_id)}, {"$set": details})
    return {"Succesfully updated the record"}

async def deleteempnoticeid(empnotice_id:str):
    col_empnotice.delete_one({'_id': ObjectId(empnotice_id)})
    return True
