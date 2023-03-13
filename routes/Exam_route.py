from fastapi import APIRouter, HTTPException  , status,Depends
from models.Exam import Exam, Exam_modify
from database.Exam_db import( 
    viewExam, 
    searchExam, 
    addExam,
    modifyExam, 
    deleteExamid
)
from database.auth import AuthHandler
auth_handler=AuthHandler()


router = APIRouter(
    prefix="/exam",
    tags=["Exam"],
    dependencies=[Depends(auth_handler.auth_wrapper)],
    responses={404: {"description": "Not found"}},)

@router.get("/" )
async def view_Exam(user=Depends(auth_handler.auth_wrapper)):
    auth_handler.has_permission(user, 'view_employee')

    response = await viewExam()
    if response: 
        return {
            "status " : status.HTTP_200_OK, 
            "Exam list" : response }
    return {"error": status.HTTP_204_NO_CONTENT} 


@router.get("/{Exam_id}")
async def search_Exam(Exam_id:str):
    # print(Exam_id)
    response = await searchExam(Exam_id)
    return response



@router.post("/")
async def create_Exam(Exam : Exam):
    response = await addExam(Exam.dict())
    if response==True:
        return {"response ": "Successfully added . . .",
            "status" : status.HTTP_200_OK}       
    return {"response" : response, "status" :status.HTTP_203_NON_AUTHORITATIVE_INFORMATION }


@router.put("/modify/{Exam_id}")
async def modify_Exam(Exam_id: str , data : Exam_modify):
    response = await modifyExam(Exam_id, data.dict(exclude_none=True))
    return response


@router.delete('/{id}')
async def delete_id(id: str):
    
    response = await deleteExamid(id)
    if not response:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'No record with id: {id} found')
    return { "Status":"Succesfully deleted ",
        "status_code " : status.HTTP_200_OK}


