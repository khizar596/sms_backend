from fastapi import APIRouter, HTTPException, status,Depends
from database.Salary_db import ( 
    addSalary,
    viewSalary,
    modifySalary,
    deleteSalaryid
)
from models.Salary2 import Salary2, Salary2_modify
from database.auth import AuthHandler
auth_handler=AuthHandler()


router = APIRouter(
    prefix="/salary",
    tags=["Salary"],
    dependencies=[Depends(auth_handler.auth_wrapper)],
    responses={404: {"description": "Not found"}},)


@router.get("/" )

async def view_Salarys_quiz(user=Depends(auth_handler.auth_wrapper)):
    auth_handler.has_permission(user, 'view_employee')

    response = await viewSalary()
    if response: 
        return {
            "status " : status.HTTP_200_OK, 
            "Salarys_quiz list" : response }
    return {"error": status.HTTP_204_NO_CONTENT} 


# @router.get("/{Salarys_quiz_id}")
# async def search_Salarys_quiz(Salarys_quiz_id:str):
#     # print(Salarys_quiz_id)
#     response = await searchSalary(Salarys_quiz_id)
#     return response



@router.post("/")
async def add_Salarys_quiz(Salarys_quiz : Salary2):
    response = await addSalary(Salarys_quiz.dict())
    if response==True:
        return {"response ": "Successfully added . . .",
            "status" : status.HTTP_200_OK}       
    return {"response" : response, "status" :status.HTTP_203_NON_AUTHORITATIVE_INFORMATION }


@router.put("/modify/{Salarys_quiz_id}")
async def modify_Salarys_quiz(Salarys_quiz_id: str , data : Salary2_modify ):
    response = await modifySalary(Salarys_quiz_id, data.dict(exclude_none=True))
    return response


@router.delete('/{id}')
async def delete_id(id: str):
    
    response = await deleteSalaryid(id)
    if not response:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'No record with id: {id} found')
    return { "Status":"Succesfully deleted ",
        "status_code " : status.HTTP_200_OK}





