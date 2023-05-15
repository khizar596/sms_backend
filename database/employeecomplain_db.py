from settings import sms_db
from fastapi import HTTPException
from bson import ObjectId
col_Emp_comp = sms_db.Emp_complain
from models.EmployeeComplain import EmployeeComplain
from database.Employee_db import col_employee as cole
from database.Admin_db import col_Admin 


async def viewEmp_comp():
    Emp_comps=[]
    cursor = col_Emp_comp.find({})

    for document in cursor:
        Employee2id_relation = cole.find_one({"_id": ObjectId(document['Employee2id'])}, {'_id': 0,'first_name':1})
        HR_relation = cole.find_one({"_id": ObjectId(document['HR2id']), 'role.0.name': 'HR'}, {'_id': 0,'first_name':1})
        Admin2id_relation = col_Admin.find_one({"_id": ObjectId(document['Admin2id']), 'role.0.name': 'Admin'}, {'_id': 0,'name':1})
        if not None and Employee2id_relation and HR_relation and Admin2id_relation:
            document['_id']=str(document['_id'])
            document['Employee2id'] = Employee2id_relation
            document['HR2id'] = HR_relation
            document['Admin2id'] = Admin2id_relation

        Emp_comps.append(document)
    return Emp_comps

async def searchEmp_comp(Emp_comp_id : str)->dict:

    document=  col_Emp_comp.find_one({"_id": ObjectId(Emp_comp_id)},{'_id': 0}) 
    
    if not document:

        raise HTTPException(status_code=404, detail="Item not found")
    Employee2id_relation = cole.find_one({"_id": ObjectId(document['Employee2id'])}, {'_id': 0,'first_name':1})
    HR_relation = cole.find_one({"_id": ObjectId(document['HR2id']), 'role.0.name': 'HR'}, {'_id': 0,'first_name':1})
    Admin2id_relation = col_Admin.find_one({"_id": ObjectId(document['Admin2id']), 'role.0.name': 'Admin'}, {'_id': 0,'name':1})
    if not None and Employee2id_relation and HR_relation and Admin2id_relation:
        document['Employee2id'] = Employee2id_relation
        document['HR2id'] = HR_relation
        document['Admin2id'] = Admin2id_relation
    return document


async def addEmp_comp(details):
    if  "Employee2id" in details:
        Employee2id_relation = cole.find_one({"_id": ObjectId(details['Employee2id'])}, {'_id': 0,'first_name':1})

        if Employee2id_relation==None:
            raise HTTPException(204, detail="Employee not found")
    if "HR2id" in details:
        HR_relation = cole.find_one({"_id": ObjectId(details['HR2id']), 'role.0.name': 'HR'}, {'_id': 0,'first_name':1})
        if HR_relation==None:
            raise HTTPException(204, detail="HR not found")
    if "Admin2id" in details:
        Admin2id_relation = col_Admin.find_one({"_id": ObjectId(details['Admin2id']), 'role.0.name': 'Admin'}, {'_id': 0,'name':1})
        
        if Admin2id_relation==None:
            raise HTTPException(204, detail="Admin not found")
    col_Emp_comp.insert_one(details) # Changing ki hab 
    return True


async def modifyEmp_comp(Emp_comp_id:str , details):
    if  "Employee2id" in details:
        Employee2id_relation = cole.find_one({"_id": ObjectId(details['Employee2id'])}, {'_id': 0,'first_name':1})

        if Employee2id_relation==None:
            del details['Employee2id']
    if "HR2id" in details:
        HR_relation = cole.find_one({"_id": ObjectId(details['HR2id']), 'role.0.name': 'HR'}, {'_id': 0,'first_name':1})
        if HR_relation==None:
            del details['HR2id']
    if "Admin2id" in details:
        Admin2id_relation = col_Admin.find_one({"_id": ObjectId(details['Admin2id']), 'role.0.name': 'Admin'}, {'_id': 0,'name':1})
        
        if Admin2id_relation==None:
            del details['Admin2id']
    
    
    col_Emp_comp.update_one({"_id": ObjectId(Emp_comp_id)}, {"$set": details})
    return {"Succesfully updated the record"}

async def deletebyid(Emp_comp_id:str):
    col_Emp_comp.delete_one({'_id': ObjectId(Emp_comp_id)})
    return True
