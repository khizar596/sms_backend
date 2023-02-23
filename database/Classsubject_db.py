from settings import sms_db
from fastapi import HTTPException
from bson import ObjectId
from models.Class_subject import Class_subject
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
    # feedetails= details
    # Student_id_check = feedetails['Studentid']
    # document=  col_student.find_one({"_id": ObjectId(Student_id_check)},{'_id': 0})    
    # if document:
    #     col_fee.insert_one(feedetails) # Changing ki hab 
    #     return True
    # return {"Id error":"Id of student doesn't exist"}

    col_Classsubject.insert_one(Classsubjectdetails) # Changing ki hab 
    return True

async def modifyClasssubject(Classsubject_id:str , details):
    col_Classsubject.update_one({"_id": ObjectId(Classsubject_id)}, {"$set": details})
    return {"Succesfully updated the record"}

async def deleteclasssubjectid(Classsubject_id:str):
    col_Classsubject.delete_one({'_id': ObjectId(Classsubject_id)})
    return True
