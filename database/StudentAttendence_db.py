from settings import sms_db
from fastapi import HTTPException
from bson import ObjectId
from database.Student_db import col_student
from models.StudentAttendence import StudentAttendence
col_STD_attendence = sms_db.Student_Attendence



async def viewSTD_attendence():
    STD_attendences=[]
    cursor = col_STD_attendence.find({})

    for document in cursor:
        STD_attendences.append((StudentAttendence(**document)))
    return STD_attendences

async def searchSTD_attendence(STD_attendence_id : str)->dict:

    document=  col_STD_attendence.find_one({"_id": ObjectId(STD_attendence_id)},{'_id': 0}) 
    
    if not document:

        raise HTTPException(status_code=404, detail="document not found")
    
    return document


async def addSTD_attendence(details):

    Student_id_check = details['Studentid'][0]
    student_found=  [col_student.find_one({"_id": ObjectId(Student_id_check)},{'_id': 0})]
    if student_found:
        details['Studentid']=student_found
        col_STD_attendence.insert_one(details) # Changing ki hab 
        return True

async def modifySTD_attendence(STD_attendence_id:str , details):
    Student_id_check = details['Studentid'][0]
    student_found=  [col_student.find_one({"_id": ObjectId(Student_id_check)},{'_id': 0})]
    if student_found:
        details['Studentid']=student_found
        col_STD_attendence.update_one({"_id": ObjectId(STD_attendence_id)}, {"$set": details})
        return {"Succesfully updated the record"}

async def deleteSTD_attendenceid(STD_attendence_id:str):
    col_STD_attendence.delete_one({'_id': ObjectId(STD_attendence_id)})
    return True
