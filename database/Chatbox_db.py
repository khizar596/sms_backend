from settings import sms_db
from fastapi import HTTPException
from models.chatbox import Chatbox
from bson import ObjectId
from database.StudentAdmin_db import col_StudentAdmin
from database.Admin_db import col_Admin
from database.Teacher_db import col_Teacher
from database.Classsubject_db import col_Classsubject
from database.Student_db import col_student
col_chatbox = sms_db.chatbox



async def viewchatbox():
    col_chatboxs=[]
   
    cursor = col_chatbox.find({})
   
    for document in cursor:
        col_chatboxs.append((Chatbox(**document)))
    return col_chatboxs
    

# async def searchchatbox(chatbox_id : str)->dict:

#     document=  col_chatbox.find_one({"_id": ObjectId(chatbox_id)},{'_id': 0}) 
    
#     if not document:

#         raise HTTPException(status_code=404, detail="document not found")
    
#     return document


async def addchatbox(details):
    chatboxdetails= details
    
    Studentid_relation=  [col_student.find_one({"_id": ObjectId( chatboxdetails['Studentid'][0])},{'_id': 0})]
    Class_subjectid_relation=  [col_Classsubject.find_one({"_id": ObjectId( chatboxdetails['Class_subjectid'][0])},{'_id': 0})]
    Teacherid_relation=  [col_Teacher.find_one({"_id": ObjectId( chatboxdetails['Teacherid'][0])},{'_id': 0})]
    Admin2id_relation=  [col_Admin.find_one({"_id": ObjectId( chatboxdetails['Admin2id'][0])},{'_id': 0})]
    StudentAdminid_relation=  [col_StudentAdmin.find_one({"_id": ObjectId( chatboxdetails['StudentAdminid'][0])},{'_id': 0})]
    if StudentAdminid_relation and Class_subjectid_relation and Admin2id_relation and Studentid_relation and Teacherid_relation:
        col_chatbox.insert_one(chatboxdetails) 
        return True
    else: 
        return False
    
    
async def modifychatbox(chatbox_id:str , details):
    col_chatbox.update_one({"_id": ObjectId(chatbox_id)}, {"$set": details})
    return {"Succesfully updated the record"}

async def deletechatboxid(chatbox_id:str):
    col_chatbox.delete_one({'_id': ObjectId(chatbox_id)})
    return True



# $$$$$$ LOGICAL AREA 

