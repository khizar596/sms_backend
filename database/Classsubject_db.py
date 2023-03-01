from settings import sms_db
from fastapi import HTTPException
from bson import ObjectId
from models.Class_subject import Class_subject
from database.Class_db import col_Class
from database.Courses_db import col_Course
from database.Teacher_db import col_Teacher
col_Classsubject = sms_db.Classsubject



async def viewClasssubject():
    Classsubjects=[]
    cursor = col_Classsubject.find({})
    
    for document in cursor:
        Classsubjects.append((Class_subject(**document)))
    return Classsubjects

async def searchClasssubject(Classsubject_id : str)->dict:

    document=  col_Classsubject.find_one({"_id": ObjectId(Classsubject_id)},{'_id': 0}) 
    
    if not document:

        raise HTTPException(status_code=404, detail="document not found")
    
    return document


async def addClasssubject(details):
    Classsubjectdetails= details
      
    class_relation=  [col_Class.find_one({"_id": ObjectId( Classsubjectdetails['Classid'][0])},{'_id': 0})]
    Teacher_relation=  [col_Class.find_one({"_id": ObjectId( Classsubjectdetails['Teacherid'][0])},{'_id': 0,'first_name':1})]

    Course_relation=  [col_Course.find_one({"_id": ObjectId( Classsubjectdetails['Courseid'][0])},{'_id': 0})] #ROLA WALA JAGA    
    if class_relation!=None or Course_relation !=None or Teacher_relation !=None :
        Classsubjectdetails['Classid'] = class_relation
        Classsubjectdetails['Courseid'] = Course_relation
        Classsubjectdetails['Teacherid'] = Teacher_relation
        col_Classsubject.insert_one(Classsubjectdetails) # Changing ki hab 
        return True

    col_Classsubject.insert_one(Classsubjectdetails) # Changing ki hab 
    return True

async def modifyClasssubject(Classsubject_id:str , details):
    Classsubjectdetails= details

    class_relation=  [col_Class.find_one({"_id": ObjectId( Classsubjectdetails['Classid'][0])},{'_id': 0})]
    Teacher_relation=  [col_Teacher.find_one({"_id": ObjectId( Classsubjectdetails['Teacherid'][0])},{'_id': 0,'first_name':1})]
    Course_relation=  [col_Course.find_one({"_id": ObjectId( Classsubjectdetails['Courseid'][0])},{'_id': 0})] #ROLA WALA JAGA    
    if class_relation!=None:
        Classsubjectdetails['Classid'] = class_relation
    if Course_relation !=None:
        Classsubjectdetails['Courseid'] = Course_relation
    if Teacher_relation !=None :
        Classsubjectdetails['Teacherid'] = Teacher_relation
    
    col_Classsubject.update_one({"_id": ObjectId(Classsubject_id)}, {"$set": details})
    return {"Succesfully updated the record"}

async def deleteclasssubjectid(Classsubject_id:str):
    col_Classsubject.delete_one({'_id': ObjectId(Classsubject_id)})
    return True
