from fastapi import APIRouter,status, HTTPException,Depends
from models.Fee import Fee ,Fee_modify
from database.Fee_db import (
    addfee,
    modifyfee,
    viewfee, 
    searchfee,
    deletebyid
)
from database.auth import AuthHandler
auth_handler=AuthHandler()



router = APIRouter(
    prefix="/fee",
    tags=["Fee Contains Student id also "],
    dependencies=[Depends(auth_handler.auth_wrapper)],
    responses={404: {"description": "Not found"}},)

@router.get("/" )
async def view_fee(user=Depends(auth_handler.auth_wrapper)):
    auth_handler.has_permission(user, 'view_employee')

    response = await viewfee()
    if response: 
        return {
            "status" : status.HTTP_200_OK, 
            "feeses" : response }
    return {"error": status.HTTP_204_NO_CONTENT} 


@router.get("/{fee_id}")
async def search_fee(fee_id:str):
    # print(fee_id)
    response = await searchfee(fee_id)
    return response



@router.post("/")
async def add_fee(fee : Fee):
    response = await addfee(fee.dict())
    if response==True:
        return {"response ": "Successfully created . . .",
            "status" : status.HTTP_200_OK}       
    return {"response" : response, "status" :status.HTTP_203_NON_AUTHORITATIVE_INFORMATION }


@router.put("/modify/{fee_id}")
async def modify_fee(fee_id: str , data :Fee_modify ):
    response = await modifyfee(fee_id, data.dict(exclude_none=True))
    return response


@router.delete('/{id}')
async def delete_id(id: str):
    
    response = await deletebyid(id)
    if not response:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'No record with id: {id} found')
    return { "status" : status.HTTP_200_OK}