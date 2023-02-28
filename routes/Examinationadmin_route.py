from fastapi import APIRouter, HTTPException, status
from models.ExaminationAdmin2 import ExaminationAdmin2 , ExaminationAdmin2_modify
from database.Examinationadmin_db import ( 
    viewExaminationadmin,
    deleteExaminationadminid,
    modifyExaminationadmin,
    searchExaminationadmin,
    addExaminationadmin

)


router = APIRouter(
    prefix="/Examinationadmin",
    tags=["Examinationadmin"],
    # dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},)


router = APIRouter(
    prefix="/Examinationadmin",
    tags=["Examinationadmin"],
    # dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},)


@router.get("/")
async def view_Examinationadmin():
    response = await viewExaminationadmin()
    print(response)
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

