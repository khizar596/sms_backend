from settings import sms_db
from fastapi import HTTPException,status
from bson import ObjectId
from database.Student_db import col_student
from models.StudentAttendence import StudentAttendence
col_STD_attendence = sms_db.Student_Attendence



async def viewSTD_attendence():
    STD_attendences=[]
    
    cursor = col_STD_attendence.find({})

    for document in cursor:
        Student_id_check = str(document['Studentid'])

        student_found=  col_student.find_one({"_id": ObjectId(Student_id_check)},{'_id': 0,'first_name':1,'last_name':1})
        if student_found:
            document['_id']=str(document['_id'])
            document['Studentid']=student_found
        STD_attendences.append(document)
    return STD_attendences

async def searchSTD_attendence(STD_attendence_id : str)->dict:

    document=  col_STD_attendence.find_one({"_id": ObjectId(STD_attendence_id)},{'_id': 0}) 

    if not document:

        raise HTTPException(status_code=404, detail="document not found")
    Student_id_check = str(document['Studentid'])

    student_found=  col_student.find_one({"_id": ObjectId(Student_id_check)},{'_id': 0})        
    document['Studentid']=student_found
    return document


async def addSTD_attendence(details):

    Student_id_check = details['Studentid']
    student_found=  col_student.find_one({"_id": ObjectId(Student_id_check)},{'_id': 0})
    if student_found:
        # details['Studentid']=student_found
        col_STD_attendence.insert_one(details) # Changing ki hab 
        return True

async def modifySTD_attendence(STD_attendence_id:str , details):
    Student_id_check = str(details['Studentid'])
    if Student_id_check:
        try:
            student_found=  col_student.find_one({"_id": ObjectId(Student_id_check)},{'_id': 0})
        except:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                detail=f'No record with id: {Student_id_check} found')
    col_STD_attendence.update_one({"_id": ObjectId(STD_attendence_id)}, {"$set": details})
    return {"Succesfully updated the record"}

async def deleteSTD_attendenceid(STD_attendence_id:str):
    col_STD_attendence.delete_one({'_id': ObjectId(STD_attendence_id)})
    return True
