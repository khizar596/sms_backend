from fastapi import APIRouter, HTTPException, status,Depends
from models.ExaminationAdmin2 import ExaminationAdmin2 , ExaminationAdmin2_modify
from database.Examinationadmin_db import ( 
    viewExaminationadmin,
    deleteExaminationadminid,
    modifyExaminationadmin,
    searchExaminationadmin,
    addExaminationadmin

)
from database.auth import AuthHandler
auth_handler=AuthHandler()


router = APIRouter(
    prefix="/Examinationadmin",
    tags=["Examinationadmin"],
    dependencies=[Depends(auth_handler.auth_wrapper)],
    responses={404: {"description": "Not found"}},)


@router.get("/")
async def view_Examinationadmin(user=Depends(auth_handler.auth_wrapper)):
    auth_handler.has_permission(user, 'view_employee')

    response = await viewExaminationadmin()
    if response: 
        return {
            "status " : status.HTTP_200_OK, 
            "Examinationadmin list" : response }
    return {"error": status.HTTP_204_NO_CONTENT} 


@router.get("/{Examinationadmin_id}")
async def search_Examinationadmin(Examinationadmin_id:str):
    # print(Examinationadmin_id)
    response = await searchExaminationadmin(Examinationadmin_id)
    return response



@router.post("/")
async def enroll_Examinationadmin(Examinationadmin : ExaminationAdmin2):
    
    response = await addExaminationadmin(Examinationadmin.dict())
    if response==True:
        return {"response ": "Successfully created . . .",
            "status" : status.HTTP_200_OK}       
    return {"response" : response, "status" :status.HTTP_203_NON_AUTHORITATIVE_INFORMATION }


@router.put("/modify/{Examinationadmin_id}")
async def modify_Examinationadmin(Examinationadmin_id: str , data :ExaminationAdmin2_modify ):
    response = await modifyExaminationadmin(Examinationadmin_id, data.dict(exclude_none=True))
    return response


@router.delete('/{id}')
async def delete_id(id: str):
    
    response = await deleteExaminationadminid(id)
    if not response:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'No record with id: {id} found')
    return { "status " : status.HTTP_200_OK}

