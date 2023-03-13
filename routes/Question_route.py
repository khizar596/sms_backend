from fastapi import APIRouter, HTTPException , status,Depends
from database.Questions_db import (
    viewQuestions_quiz, 
    modifyQuestions_quiz,
    deletebyid,
    searchQuestions_quiz,
    createQuestions_quiz
)
from models.Questions import Question, Question_modify
from database.auth import AuthHandler
auth_handler=AuthHandler()


router = APIRouter(
    prefix="/question",
    tags=["Question  related  to quizz"],
    dependencies=[Depends(auth_handler.auth_wrapper)],
    responses={404: {"description": "Not found"}},)

@router.get("/" )
async def view_Questions_quiz(user=Depends(auth_handler.auth_wrapper)):
    auth_handler.has_permission(user, 'view_employee')

    
    response = await viewQuestions_quiz()
    if response: 
        return {
            "status " : status.HTTP_200_OK, 
            "Questions_quiz list" : response }
    return {"error": status.HTTP_204_NO_CONTENT} 


@router.get("/{Questions_quiz_id}")
async def search_Questions_quiz(Questions_quiz_id:str):
    # print(Questions_quiz_id)
    response = await searchQuestions_quiz(Questions_quiz_id)
    return response



@router.post("/")
async def add_Questions_quiz(Questions_quiz : Question):
    response = await createQuestions_quiz(Questions_quiz.dict())
    if response==True:
        return {"response ": "Successfully added . . .",
            "status" : status.HTTP_200_OK}       
    return {"response" : response, "status" :status.HTTP_203_NON_AUTHORITATIVE_INFORMATION }


@router.put("/modify/{Questions_quiz_id}")
async def modify_Questions_quiz(Questions_quiz_id: str , data :Question_modify ):
    response = await modifyQuestions_quiz(Questions_quiz_id, data.dict(exclude_none=True))
    return response


@router.delete('/{id}')
async def delete_id(id: str):
    
    response = await deletebyid(id)
    if not response:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'No record with id: {id} found')
    return { "Status":"Succesfully deleted ",
        "status_code " : status.HTTP_200_OK}