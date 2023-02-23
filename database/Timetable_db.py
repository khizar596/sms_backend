from settings import sms_db
from fastapi import HTTPException
from models.Timetable import Timetable
from bson import ObjectId
col_timetable = sms_db.Timetable



async def viewtimetable():
    col_timetables=[]
   
    cursor = col_timetable.find({})
   
    for document in cursor:
        col_timetables.append((Timetable(**document)))
    return col_timetables
    

async def searchtimetable(timetable_id : str)->dict:

    document=  col_timetable.find_one({"_id": ObjectId(timetable_id)},{'_id': 0}) 
    
    if not document:

        raise HTTPException(status_code=404, detail="document not found")
    
    return document


async def addtimetable(details):
    timetabledetails= details
    # feedetails= details
    # Student_id_check = feedetails['Studentid']
    # document=  col_student.find_one({"_id": ObjectId(Student_id_check)},{'_id': 0})    
    # if document:
    #     col_fee.insert_one(feedetails) # Changing ki hab 
    #     return True
    # return {"Id error":"Id of student doesn't exist"}

    col_timetable.insert_one(timetabledetails) # Changing ki hab 
    return True

async def modifytimetable(timetable_id:str , details):
    col_timetable.update_one({"_id": ObjectId(timetable_id)}, {"$set": details})
    return {"Succesfully updated the record"}

async def deletetimetableid(timetable_id:str):
    col_timetable.delete_one({'_id': ObjectId(timetable_id)})
    return True
