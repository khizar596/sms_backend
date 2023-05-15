from settings import sms_db
from fastapi import HTTPException
from bson import ObjectId
from database.Admin_db import col_Admin
from database.Student_db import col_student
from database.StudentAdmin_db import col_employee
# is k andr studnet admin ko complete kr k  dalna ha 
col_Std_comp = sms_db.Std_complain
from models.StudentComplain import StudentComplain



async def viewStd_comp():
    Emp_comps=[]
    cursor = col_Std_comp.find({})

    for document in cursor:
        Student2id_relation = col_student.find_one({"_id": ObjectId(document['Studentid'])}, {'_id': 0,'first_name':1})
        STdadm_relation = col_employee.find_one({"_id": ObjectId(document['StudentAdminid']), 'role.0.name': 'Student Admin'}, {'_id': 0,'first_name':1})
        Admin2id_relation = col_Admin.find_one({"_id": ObjectId(document['Admin2id']), 'role.0.name': 'Admin'}, {'_id': 0,'name':1})
        if not None and Student2id_relation and STdadm_relation and Admin2id_relation:
            document['_id']=str(document['_id'])
            document['Studentid'] = Student2id_relation
            document['StudentAdminid'] = STdadm_relation
            document['Admin2id'] = Admin2id_relation
            document['_id']=str(document['_id'])

        Emp_comps.append(document)
    return Emp_comps

async def searchStd_comp(Std_comp_id : str)->dict:

    document=  col_Std_comp.find_one({"_id": ObjectId(Std_comp_id)}) 
    
    if not document:

        raise HTTPException(status_code=404, detail="Item not found")
    Student2id_relation = col_student.find_one({"_id": ObjectId(document['Studentid'])}, {'_id': 0,'first_name':1})
    STdadm_relation = col_employee.find_one({"_id": ObjectId(document['StudentAdminid']), 'role.0.name': 'Student Admin'}, {'_id': 0,'first_name':1})
    Admin2id_relation = col_Admin.find_one({"_id": ObjectId(document['Admin2id']), 'role.0.name': 'Admin'}, {'_id': 0,'name':1})
    if not None and Student2id_relation and STdadm_relation and Admin2id_relation:
        document['_id']=str(document['_id'])
        document['Studentid'] = Student2id_relation
        document['StudentAdminid'] = STdadm_relation
        document['Admin2id'] = Admin2id_relation
    return document

async def addStd_comp(details):
    if  "Studentid" in details:
        Studentid_relation = col_student.find_one({"_id": ObjectId(details['Studentid'])}, {'_id': 0,'first_name':1})

        if Studentid_relation==None:
            raise HTTPException(204, detail="Employee not found")
    if "StudentAdminid" in details:
        stdadm_relation = col_employee.find_one({"_id": ObjectId(details['StudentAdminid']), 'role.0.name': 'Student Admin'}, {'_id': 0,'first_name':1})
        if stdadm_relation==None:
            raise HTTPException(204, detail="stdadm not found")
    if "Admin2id" in details:
        Admin2id_relation = col_Admin.find_one({"_id": ObjectId(details['Admin2id']), 'role.0.name': 'Admin'}, {'_id': 0,'name':1})
        
        if Admin2id_relation==None:
            raise HTTPException(204, detail="Admin not found")
    col_Std_comp.insert_one(details) 
    return True
    
    
async def modifyStd_comp(Std_comp_id:str , details):
    if  "Studentid" in details:
        Studentid_relation = col_student.find_one({"_id": ObjectId(details['Studentid'])}, {'_id': 0,'first_name':1})

        if Studentid_relation==None:
            del details['Studentid']
    if "StudentAdminid" in details:
        HR_relation = col_employee.find_one({"_id": ObjectId(details['StudentAdminid']), 'role.0.name': 'HR'}, {'_id': 0,'first_name':1})
        if HR_relation==None:
            del details['StudentAdminid']
    if "Admin2id" in details:
        Admin2id_relation = col_Admin.find_one({"_id": ObjectId(details['Admin2id']), 'role.0.name': 'Admin'}, {'_id': 0,'name':1})
        
        if Admin2id_relation==None:
            del details['Admin2id']
    
    
    col_Std_comp.update_one({"_id": ObjectId(Std_comp_id)}, {"$set": details})
    return {"Succesfully updated the record"}

async def deletebyid(Std_comp_id:str):
    col_Std_comp.delete_one({'_id': ObjectId(Std_comp_id)})
    return True
