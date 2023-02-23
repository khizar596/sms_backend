from settings import sms_db
from fastapi import HTTPException
from bson import ObjectId
from models.Quiz import Quiz 
col_Quizz = sms_db.Quizz



async def viewQuizz():
    Quizzs=[]
    cursor = col_Quizz.find({})

    for document in cursor:
        Quizzs.append((Quiz(**document)))
    return Quizzs

# async def searchQuizz(Quizz_id : str)->dict:

#     document=  col_Quizz.find_one({"_id": ObjectId(Quizz_id)},{'_id': 0}) 
    
#     if not document:

#         raise HTTPException(status_code=404, detail="document not found")
    
#     return document


async def addQuizz(details):
    Quizzdetails= details
    
    col_Quizz.insert_one(Quizzdetails) # Changing ki hab 
    return True

async def modifyQuizz(Quizz_id:str , details):
    col_Quizz.update_one({"_id": ObjectId(Quizz_id)}, {"$set": details})
    return {"Succesfully updated the record"}

async def deleteQuizzid(Quizz_id:str):
    col_Quizz.delete_one({'_id': ObjectId(Quizz_id)})
    return True
