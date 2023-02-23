from settings import sms_db
from fastapi import HTTPException
from bson import ObjectId
from models.Courses import Courses
col_Course = sms_db.Course



async def viewCourse():
    Coursses=[]
    cursor = col_Course.find({})

    for document in cursor:
        Coursses.append((Courses(**document)))
    return Coursses

async def searchCourse(Course_id : str)->dict:

    document=  col_Course.find_one({"_id": ObjectId(Course_id)},{'_id': 0}) 
    
    if not document:

        raise HTTPException(status_code=404, detail="document not found")
    
    return document


async def addCourse(details):
    Coursedetails= details
    
    col_Course.insert_one(Coursedetails) # Changing ki hab 
    return True

async def modifyCourse(Course_id:str , details):
    col_Course.update_one({"_id": ObjectId(Course_id)}, {"$set": details})
    return {"Succesfully updated the record"}

async def deleteCourseid(Course_id:str):
    col_Course.delete_one({'_id': ObjectId(Course_id)})
    return True
