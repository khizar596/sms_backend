from fastapi import APIRouter, HTTPException , status,Depends
from database.StudentComplain_db import (
    viewStd_comp, 
    modifyStd_comp,
    deletebyid,
    searchStd_comp,
    addStd_comp
)
from models.StudentComplain import StudentComplain, StudentComplain_modify
from database.auth import AuthHandler
auth_handler=AuthHandler()

router = APIRouter(
    prefix="/stdcomplain",
    tags=["Student Complaint"],
    dependencies=[Depends(auth_handler.auth_wrapper)],
    responses={404: {"description": "Not found"}})


@router.get("/" )
async def view_Std_comp(user=Depends(auth_handler.auth_wrapper)):
    auth_handler.has_permission(user, 'view_employee')

    response = await viewStd_comp()
    if response: 
        return {
            "status" : status.HTTP_200_OK, 
            "Std_comps" : response }
    return {"error": status.HTTP_204_NO_CONTENT} 


@router.get("/{Std_comp_id}")
async def search_Std_comp(Std_comp_id:str):
    # print(Std_comp_id)
    response = await searchStd_comp(Std_comp_id)
    return response



@router.post("/")
async def add_Std_comp(Std_comp : StudentComplain):
    response = await addStd_comp(Std_comp.dict())
    if response==True:
        return {"response ": "Successfully created . . .",
            "status" : status.HTTP_200_OK}       
    return {"response" : response, "status" :status.HTTP_203_NON_AUTHORITATIVE_INFORMATION }


@router.put("/modify/{Std_comp_id}")
async def modify_Std_comp(Std_comp_id: str , data :StudentComplain_modify ):
    response = await modifyStd_comp(Std_comp_id, data.dict(exclude_none=True))
    return response


@router.delete('/{id}')
async def delete_id(id: str):
    
    response = await deletebyid(id)
    if not response:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'No record with id: {id} found')
    return { "Status":"Succesfully deleted ",
        "status_code" : status.HTTP_200_OK}