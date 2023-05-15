from settings import sms_db
from fastapi import HTTPException
from bson import ObjectId
from models.Quiz import Quiz 
from database.Classsubject_db import col_Classsubject
col_Quizz = sms_db.Quizz



async def viewQuizz():
    Quizzs=[]
    cursor = col_Quizz.find({})
   
    for document in cursor:
        Student_id_check = str(document['Class_subjectid'])
        try:
            subject_found=  col_Classsubject.find_one({"_id": ObjectId(Student_id_check)},{'_id': 0})
        except:
            raise HTTPException(204,f"Subject id not found for {str(document['_id'])}")
        document['Class_subjectid'] = subject_found
        document['_id']=str(document['_id'])
        Quizzs.append(document)
    return Quizzs

async def searchQuizz(Quizz_id : str)->dict:

    document=  col_Quizz.find_one({"_id": ObjectId(Quizz_id)},{'_id': 0}) 
    if document is not None:
        Student_id_check = str(document['Class_subjectid'])
        try:
            subject_found=  col_Classsubject.find_one({"_id": ObjectId(Student_id_check)},{'_id': 0})
            document['Class_subjectid'] = subject_found
        except:
            raise HTTPException(204,f"Subjecti if for {document['_id']}")
        if not document:

            raise HTTPException(status_code=404, detail="document not found")
        
        return document
    raise HTTPException(204,"Details not found")

async def addQuizz(details):
    Student_id_check = str(details['Class_subjectid'])
    try:
        subject_found=  col_Classsubject.find_one({"_id": ObjectId(Student_id_check)},{'_id': 0}) 
    except:
        raise HTTPException(204,f"subject id not found")
    if subject_found!=None:
        col_Quizz.insert_one(details) 
        return True        
    else:
        raise HTTPException(204,"details are not correct")

async def modifyQuizz(Quizz_id:str , details):
    if "Class_subjectid" in details:
        try:
            subject_found=  col_Classsubject.find_one({"_id": ObjectId(Quizz_id)},{'_id': 0}) 
        except:
            raise HTTPException(204,f"subject id not found")
        
    col_Quizz.update_one({"_id": ObjectId(Quizz_id)}, {"$set": details})
    return {"Succesfully updated the record"}

async def deleteQuizzid(Quizz_id:str):
    col_Quizz.delete_one({'_id': ObjectId(Quizz_id)})
    return True
