from settings import sms_db
from fastapi import HTTPException
from models.chatbox import Chatbox
from bson import ObjectId
from database.Admin_db import col_Admin
from database.Teacher_db import col_employee as cole
from database.Classsubject_db import col_Classsubject
from database.Student_db import col_student
col_chatbox = sms_db.chatbox



async def viewchatbox():
    col_chatboxs = []
    cursor = col_chatbox.find({})
    for document in cursor:
        
        Studentid_relation = col_student.find_one({"_id": ObjectId(document['Studentid'])}, {'_id': 0,'first_name':1})
        Class_subjectid_relation = col_Classsubject.find_one({"_id": ObjectId(document['Class_subjectid'])}, {'_id': 0})
        Teacherid_relation = cole.find_one({"_id": ObjectId(document['Teacherid']), 'role.0.name': 'Teacher'}, {'_id': 0,'first_name':1})
        Admin2id_relation = col_Admin.find_one({"_id": ObjectId(document['Admin2id']), 'role.0.name': 'Admin'}, {'_id': 0,'name':1})
        StudentAdminid_relation = cole.find_one({"_id": ObjectId(document['StudentAdminid']), 'role.0.name': 'Student Admin'}, {'_id': 0,'first_name':1})

        if not None and StudentAdminid_relation and Class_subjectid_relation and Admin2id_relation and Studentid_relation and Teacherid_relation:
            document['_id']=str(document['_id'])
            document['Studentid'] = Studentid_relation
            document['Class_subjectid'] = Class_subjectid_relation
            document['Teacherid'] = Teacherid_relation
            document['Admin2id'] = Admin2id_relation
            document['StudentAdminid'] = StudentAdminid_relation
            col_chatboxs.append(document)
    return col_chatboxs

async def searchchatbox(chatbox_id : str)->dict:

    document=  col_chatbox.find_one({"_id": ObjectId(chatbox_id)},{'_id': 0}) 
    
    if not document:

        raise HTTPException(status_code=404, detail="document not found")
    Studentid_relation = col_student.find_one({"_id": ObjectId(document['Studentid'])}, {'_id': 0,'first_name':1})
    Class_subjectid_relation = col_Classsubject.find_one({"_id": ObjectId(document['Class_subjectid'])}, {'_id': 0})
    Teacherid_relation = cole.find_one({"_id": ObjectId(document['Teacherid']), 'role.0.name': 'Teacher'}, {'_id': 0,'first_name':1})
    Admin2id_relation = col_Admin.find_one({"_id": ObjectId(document['Admin2id']), 'role.0.name': 'Admin'}, {'_id': 0,'name':1})
    StudentAdminid_relation = cole.find_one({"_id": ObjectId(document['StudentAdminid']), 'role.0.name': 'Student Admin'}, {'_id': 0,'first_name':1})
    if not None and StudentAdminid_relation and Class_subjectid_relation and Admin2id_relation and Studentid_relation and Teacherid_relation:
        document['Studentid']=Studentid_relation
        document['Class_subjectid']=Class_subjectid_relation
        document['Teacherid']=Teacherid_relation
        document['Admin2id']=Admin2id_relation
        document['StudentAdminid']=StudentAdminid_relation
        return document
    else : 
        raise LookupError

async def addchatbox(details):
    chatboxdetails= details
    
    Studentid_relation = col_student.find_one({"_id": ObjectId(chatboxdetails['Studentid'])}, {'_id': 0,'first_name':1})
    Class_subjectid_relation = col_Classsubject.find_one({"_id": ObjectId(chatboxdetails['Class_subjectid'])}, {'_id': 0})
    Teacherid_relation = cole.find_one({"_id": ObjectId(chatboxdetails['Teacherid']), 'role.0.name': 'Teacher'}, {'_id': 0,'first_name':1})
    Admin2id_relation = col_Admin.find_one({"_id": ObjectId(chatboxdetails['Admin2id']), 'role.0.name': 'Admin'}, {'_id': 0,'name':1})
    StudentAdminid_relation = cole.find_one({"_id": ObjectId(chatboxdetails['StudentAdminid']), 'role.0.name': 'Student Admin'}, {'_id': 0,'first_name':1})



    if not None and StudentAdminid_relation and Class_subjectid_relation and Admin2id_relation and Studentid_relation and Teacherid_relation:
        
        col_chatbox.insert_one(chatboxdetails) 
        return True
    else: 
        return False
    
    
async def modifychatbox(chatbox_id:str , details):
    chatboxdetails= details

    if  "Studentid" in details:
        Studentid_relation = col_student.find_one({"_id": ObjectId(chatboxdetails['Studentid'])}, {'_id': 0,'first_name':1})

        if Studentid_relation==None:
            del details['Studentid']
    if "Class_subjectid" in details:
        Class_subjectid_relation = col_Classsubject.find_one({"_id": ObjectId(chatboxdetails['Class_subjectid'])}, {'_id': 0})
        if Class_subjectid_relation==None:
            del details['Class_subjectid']
    if "Admin2id" in details:
        Admin2id_relation = col_Admin.find_one({"_id": ObjectId(chatboxdetails['Admin2id']), 'role.0.name': 'Admin'}, {'_id': 0,'name':1})
        
        if Admin2id_relation==None:
            del details['Admin2id']
    if "StudentAdminid" in details:
        StudentAdminid_relation = cole.find_one({"_id": ObjectId(chatboxdetails['StudentAdminid']), 'role.0.name': 'Student Admin'}, {'_id': 0,'first_name':1})
    
        if StudentAdminid_relation==None:
            del details['StudentAdminid']
    
    
    
    col_chatbox.update_one({"_id": ObjectId(chatbox_id)}, {"$set": details})
    return {"Succesfully updated the record"}

async def deletechatboxid(chatbox_id:str):
    col_chatbox.delete_one({'_id': ObjectId(chatbox_id)})
    return True




