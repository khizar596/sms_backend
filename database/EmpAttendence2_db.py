from settings import sms_db
from database.Employee_db import col_employee as cole
from database.Admin_db import col_Admin 
from fastapi import HTTPException
from bson import ObjectId
from models.employeeattendance2 import employeeattendance2
col_Emp_Attendence2 = sms_db.Emp_Attendence2



async def viewEmp_Attendence2():
    Emp_Attendence2s=[]
    cursor = col_Emp_Attendence2.find({})

    for document in cursor:
        Employee2id_relation = cole.find_one({"_id": ObjectId(document['Employee2id'])}, {'_id': 0,'first_name':1})
        HR_relation = cole.find_one({"_id": ObjectId(document['HR2id']), 'role.0.name': 'HR'}, {'_id': 0,'first_name':1})
        Admin2id_relation = col_Admin.find_one({"_id": ObjectId(document['Admin2id']), 'role.0.name': 'Admin'}, {'_id': 0,'name':1})
        if not None and Employee2id_relation and HR_relation and Admin2id_relation:
            document['_id']=str(document['_id'])
            document['Employee2id'] = Employee2id_relation
            document['HR2id'] = HR_relation
            document['Admin2id'] = Admin2id_relation
        Emp_Attendence2s.append(document)
    return Emp_Attendence2s

async def searchEmp_Attendence2(Emp_Attendence2_id : str)->dict:

    document=  col_Emp_Attendence2.find_one({"_id": ObjectId(Emp_Attendence2_id)},{'_id': 0}) 
    
    if not document:

        raise HTTPException(status_code=404, detail="document not found")
    Employee2id_relation = cole.find_one({"_id": ObjectId(document['Employee2id'])}, {'_id': 0,'first_name':1})
    HR_relation = cole.find_one({"_id": ObjectId(document['HR2id']), 'role.0.name': 'HR'}, {'_id': 0,'first_name':1})
    Admin2id_relation = col_Admin.find_one({"_id": ObjectId(document['Admin2id']), 'role.0.name': 'Admin'}, {'_id': 0,'name':1})
    if not None and Employee2id_relation and HR_relation and Admin2id_relation:
        document['_id']=str(document['_id'])
        document['Employee2id'] = Employee2id_relation
        document['HR2id'] = HR_relation
        document['Admin2id'] = Admin2id_relation
    return document


async def addEmp_Attendence2(details):
    if  "Employee2id" in details:
        try:
            Employee2id_relation = cole.find_one({"_id": ObjectId(details['Employee2id'])}, {'_id': 0,'first_name':1})
            if Employee2id_relation==None:
                raise HTTPException(204, detail="check your Employee id")
        except:
            raise HTTPException(204, detail= "Id not found")
    if "HR2id" in details:
        try:
            HR_relation = cole.find_one({"_id": ObjectId(details['HR2id']), 'role.0.name': 'HR'}, {'_id': 0,'first_name':1})
            if HR_relation==None:
                raise HTTPException(204, detail="check your HR id")
        except:
            raise HTTPException(204, detail= "Id not found")
    if "Admin2id" in details:
        try:
            Admin2id_relation = col_Admin.find_one({"_id": ObjectId(details['Admin2id']), 'role.0.name': 'Admin'}, {'_id': 0,'name':1})
            
            if Admin2id_relation==None:
                raise HTTPException(204, detail="check your Admin id")
        except:
            raise HTTPException(204, detail= "Id not found")
    col_Emp_Attendence2.insert_one(details) # Changing ki hab 
    return True

async def modifyEmp_Attendence2(Emp_Attendence2_id:str , details):
    
    if  "Employee2id" in details:
        try:
            Employee2id_relation = cole.find_one({"_id": ObjectId(details['Employee2id'])}, {'_id': 0,'first_name':1})
            if Employee2id_relation==None:
                raise HTTPException(204, detail="check your Employee id")
        except:
            del details['Employee2id']
    if "HR2id" in details:
        try:
            HR_relation = cole.find_one({"_id": ObjectId(details['HR2id']), 'role.0.name': 'HR'}, {'_id': 0,'first_name':1})
            if HR_relation==None:
                raise HTTPException(204, detail="check your HR id")
        except:
            del details['HR2id']
    if "Admin2id" in details:
        try:
            Admin2id_relation = col_Admin.find_one({"_id": ObjectId(details['Admin2id']), 'role.0.name': 'Admin'}, {'_id': 0,'name':1})
            
            if Admin2id_relation==None:
                raise HTTPException(204, detail="check your Admin id")
        except:
            del details['Admin2id']

    
    
    
    col_Emp_Attendence2.update_one({"_id": ObjectId(Emp_Attendence2_id)}, {"$set": details})
    return {"Succesfully updated the record"}

async def deleteEmp_Attendence2id(Emp_Attendence2_id:str):
    col_Emp_Attendence2.delete_one({'_id': ObjectId(Emp_Attendence2_id)})
    return True
