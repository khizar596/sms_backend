from settings import sms_db
from fastapi import HTTPException
from bson import ObjectId
from models.Exam import Exam
col_Exam = sms_db.Exam



async def viewExam():
    Exams=[]
    cursor = col_Exam.find({})

    for document in cursor:
        document['_id']=str(document['_id'])
        Exams.append(document)
    return Exams

async def searchExam(Exam_id : str)->dict:

    document=  col_Exam.find_one({"_id": ObjectId(Exam_id)},{'_id': 0}) 
    
    if not document:

        raise HTTPException(status_code=404, detail="document not found")
    
    return document


async def addExam(details):
    Examdetails= details
    
    col_Exam.insert_one(Examdetails) # Changing ki hab 
    return True

async def modifyExam(Exam_id:str , details):
    col_Exam.update_one({"_id": ObjectId(Exam_id)}, {"$set": details})
    return {"Succesfully updated the record"}

async def deleteExamid(Exam_id:str):
    col_Exam.delete_one({'_id': ObjectId(Exam_id)})
    return True
