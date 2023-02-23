from settings import sms_db
from fastapi import HTTPException
from models.Questions import Question
from bson import ObjectId
col_Questions_quiz = sms_db.QuestionsQuiz



async def viewQuestions_quiz():
    Questions_quizs=[]
    cursor = col_Questions_quiz.find({})

    for document in cursor:
        Questions_quizs.append((Question(**document)))
    return Questions_quizs

async def searchQuestions_quiz(Questions_quiz_id : str)->dict:

    document=  col_Questions_quiz.find_one({"_id": ObjectId(Questions_quiz_id)},{'_id': 0}) 
    
    if not document:

        raise HTTPException(status_code=404, detail="Item not found")
    
    return document


async def createQuestions_quiz(details):
    Questions_quizdetails= details
    # feedetails= details
    # Student_id_check = feedetails['Studentid']
    # document=  col_student.find_one({"_id": ObjectId(Student_id_check)},{'_id': 0})    
    # if document:
    #     col_fee.insert_one(feedetails) # Changing ki hab 
    #     return True
    # return {"Id error":"Id of student doesn't exist"}

    col_Questions_quiz.insert_one(Questions_quizdetails) # Changing ki hab 
    return True

async def modifyQuestions_quiz(Questions_quiz_id:str , details):
    col_Questions_quiz.update_one({"_id": ObjectId(Questions_quiz_id)}, {"$set": details})
    return {"Succesfully updated the record"}

async def deletebyid(Questions_quiz_id:str):
    col_Questions_quiz.delete_one({'_id': ObjectId(Questions_quiz_id)})
    return True
