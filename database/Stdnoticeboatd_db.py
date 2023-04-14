from settings import sms_db
from bson import ObjectId
from models.StudentNoticeboard import StudentNoticeboard   
col_stdnotice = sms_db.Student_Noticeboard
from database.Admin_db import col_Admin
from database.StudentAdmin_db import col_StudentAdmin,col_employee
from fastapi import HTTPException

async def viewstdnotice():
    stdnotices=[]
    cursor = col_stdnotice.find({})

    for document in cursor:
        Admin2id_relation = col_Admin.find_one({"_id": ObjectId(document['Admin2id']), 'role.0.name': 'Admin'}, {'_id': 0,'name':1})
        StudentAdminid_relation = col_employee.find_one({"_id": ObjectId(document['StudentAdminid']), 'role.0.name': 'Student Admin'}, {'_id': 0,'first_name':1})
        if not None and StudentAdminid_relation and Admin2id_relation:
            document['Admin2id'] = Admin2id_relation
            document['StudentAdminid'] = StudentAdminid_relation     
            document['_id']= str(document['_id'])
            stdnotices.append(document)
    return stdnotices

async def searchstdnotice(stdnotice_id : str)->dict:

    document=  col_stdnotice.find_one({"_id": ObjectId(stdnotice_id)},{'_id': 0}) 
    
    if not document:

        raise HTTPException(status_code=404, detail="document not found")
    Admin2id_relation = col_Admin.find_one({"_id": ObjectId(document['Admin2id']), 'role.0.name': 'Admin'}, {'_id': 0,'name':1})
    StudentAdminid_relation = col_employee.find_one({"_id": ObjectId(document['StudentAdminid']), 'role.0.name': 'Student Admin'}, {'_id': 0,'first_name':1})
    if not None and StudentAdminid_relation and Admin2id_relation:
        document['Admin2id'] = Admin2id_relation
        document['StudentAdminid'] = StudentAdminid_relation     
        document['_id']= str(document['_id'])
    return document


async def addstdnotice(details):
    stdnoticedetails= details
    try:
        Admin_relation=  col_Admin.find_one({"_id": ObjectId( stdnoticedetails['Admin2id'][0])},{'_id': 0})
        StdAdmin_relation=  col_StudentAdmin.find_one({"_id": ObjectId( stdnoticedetails['StudentAdminid'][0])},{'_id': 0})
        if not None and (Admin_relation and StdAdmin_relation):
            # stdnoticedetails['Admin2id'] = Admin_relation
            # stdnoticedetails['StudentAdminid'] = StdAdmin_relation
            col_stdnotice.insert_one(stdnoticedetails) 
            return True
    except:
        raise HTTPException(status_code=203)
async def modifystdnotice(stdnotice_id:str , details):
    Admin2id_relation = col_Admin.find_one({"_id": ObjectId(details['Admin2id']), 'role.0.name': 'Admin'}, {'_id': 0,'name':1})
    StudentAdminid_relation = col_employee.find_one({"_id": ObjectId(details['StudentAdminid']), 'role.0.name': 'Student Admin'}, {'_id': 0,'first_name':1})
       
    if Admin2id_relation:
            pass
    if StudentAdminid_relation:
        pass
    col_stdnotice.update_one({"_id": ObjectId(stdnotice_id)}, {"$set": details})
    return {"Succesfully updated the record"}

async def deletestdnoticeid(stdnotice_id:str):
    col_stdnotice.delete_one({'_id': ObjectId(stdnotice_id)})
    return True
