from settings import sms_db
from fastapi import HTTPException
from models.Questions import Question
from bson import ObjectId
from database.Quizz_db import col_Quizz
col_Questions_quiz = sms_db.QuestionsQuiz



async def viewQuestions_quiz():
    Questions_quizs=[]
    cursor = col_Questions_quiz.find({})

    for document in cursor:
        quizzid_check = str(document['Quizz_id'])
        try:
            subject_found=  col_Quizz.find_one({"_id": ObjectId(quizzid_check)},{'_id': 0})
        except:
            raise HTTPException(204,f"Quizz id not found for {str(document['_id'])}")
        document['Quizz_id'] = subject_found
        document['_id']=str(document['_id'])
        Questions_quizs.append(document)
    return Questions_quizs

async def searchQuestions_quiz(Questions_quiz_id : str)->dict:

    document=  col_Questions_quiz.find_one({"_id": ObjectId(Questions_quiz_id)},{'_id': 0}) 
    if document is not None:
        quizzid_check = str(document['Quizz_id'])
        try:
            subject_found=  col_Quizz.find_one({"_id": ObjectId(quizzid_check)},{'_id': 0})
        except:
            raise HTTPException(204,f"Quizz id not found for {str(document['_id'])}")
        document['Quizz_id'] = subject_found
    if not document:

        raise HTTPException(status_code=404, detail="Item not found")
    
    return document


async def createQuestions_quiz(details):
    quizid_check = details['Quizz_id']
    try:
        document=  col_Quizz.find_one({"_id": ObjectId(quizid_check)},{'_id': 0})    
    except:
        raise HTTPException(204, 'Details of Quizz not found')
    if document!=None:
        col_Questions_quiz.insert_one(details) # Changing ki hab 
        return True
    return {"Id error":"Id of student doesn't exist"}

async def modifyQuestions_quiz(Questions_quiz_id:str , details):
    if "Quizz_id" in details:
        quizid_check = details['Quizz_id']
        try:
            document=  col_Quizz.find_one({"_id": ObjectId(quizid_check)},{'_id': 0})    
        except:
            raise HTTPException(204, 'Details of Quizz not found')
    col_Questions_quiz.update_one({"_id": ObjectId(Questions_quiz_id)}, {"$set": details})
    return {"Succesfully updated the record"}

async def deletebyid(Questions_quiz_id:str):
    col_Questions_quiz.delete_one({'_id': ObjectId(Questions_quiz_id)})
    return True
