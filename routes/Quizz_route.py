from fastapi import APIRouter, HTTPException , status,Depends
from database.Quizz_db import (
    viewQuizz,
    modifyQuizz,
    searchQuizz,
    deleteQuizzid,
    addQuizz
    )
from models.Quiz import Quiz, Quiz_modify
from database.auth import AuthHandler
auth_handler=AuthHandler()


router = APIRouter(
    prefix="/Quizz",
    tags=["Quizz  related  to quizz"],
    dependencies=[Depends(auth_handler.auth_wrapper)],
    responses={404: {"description": "Not found"}},)

@router.get("/" )
async def view_Quizzs_quiz(user=Depends(auth_handler.auth_wrapper)):
    auth_handler.has_permission(user, 'view_employee')

    response = await viewQuizz()
    if response: 
        return {
            "status" : status.HTTP_200_OK, 
            "Quizzes" : response }
    return {"error": status.HTTP_204_NO_CONTENT} 


@router.get("/{Quizzs_quiz_id}")
async def search_Quizzs_quiz(Quizzs_quiz_id:str):
    # print(Quizzs_quiz_id)
    response = await searchQuizz(Quizzs_quiz_id)
    return response



@router.post("/")
async def add_Quizzs_quiz(Quizzs_quiz : Quiz):
    response = await addQuizz(Quizzs_quiz.dict())
    if response==True:
        return {"response ": "Successfully added . . .",
            "status" : status.HTTP_200_OK}       
    return {"response" : response, "status" :status.HTTP_203_NON_AUTHORITATIVE_INFORMATION }


@router.put("/modify/{Quizzs_quiz_id}")
async def modify_Quizzs_quiz(Quizzs_quiz_id: str , data :Quiz_modify ):
    response = await modifyQuizz(Quizzs_quiz_id, data.dict(exclude_none=True))
    return response


@router.delete('/{id}')
async def delete_id(id: str):
    
    response = await deleteQuizzid(id)
    if not response:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'No record with id: {id} found')
    return { "Status":"Succesfully deleted ",
        "status_code " : status.HTTP_200_OK}