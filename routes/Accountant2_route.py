from fastapi import APIRouter, HTTPException, status,Depends
from models.Accountant2 import Accountant2 , Accountant2_modify
from database.Accountant2_db import ( 
    viewAccountant2,
    deleteAccountant2id,
    modifyAccountant2,
    searchAccountant2,
    addAccountant2

)
from database.auth import AuthHandler
auth_handler=AuthHandler()


router = APIRouter(
    prefix="/Accountant2",
    tags=["Accountant2"],
    dependencies=[Depends(auth_handler.auth_wrapper)],
    responses={404: {"description": "Not found"}})


@router.get("/")
async def view_Accountant2(user = Depends(auth_handler.auth_wrapper)):
    auth_handler.has_permission(user, 'view_accountant')
    # 'search_accountant','add_accountant', 'modify_accountant','view_accountant','delete_accountant',

    response = await viewAccountant2()
    if response: 
        return {
            "status" : status.HTTP_200_OK, 
            "Accountants" : response }
    return {"error": status.HTTP_204_NO_CONTENT} 


@router.get("/{Accountant2_id}")
async def search_Accountant2(Accountant2_id:str,user = Depends(auth_handler.auth_wrapper)):
    auth_handler.has_permission(user, 'search_accountant')
    response = await searchAccountant2(Accountant2_id)
    return response



@router.post("/")
async def enroll_Accountant2(Accountant2 : Accountant2,user = Depends(auth_handler.auth_wrapper)):
    auth_handler.has_permission(user, 'add_accountant')

    response = await addAccountant2(Accountant2.dict())
    if response==True:
        return {"response ": "Successfully created . . .",
            "status" : status.HTTP_200_OK}       
    return {"response" : response, "status" :status.HTTP_203_NON_AUTHORITATIVE_INFORMATION }


@router.put("/modify/{Accountant2_id}")
async def modify_Accountant2(Accountant2_id: str , data :Accountant2_modify,user = Depends(auth_handler.auth_wrapper) ):
    auth_handler.has_permission(user, 'modify_accountant')

    response = await modifyAccountant2(Accountant2_id, data.dict(exclude_none=True))
    return response


@router.delete('/{id}')
async def delete_id(id: str,user = Depends(auth_handler.auth_wrapper)):
    auth_handler.has_permission(user, 'delete_accountant')

    response = await deleteAccountant2id(id)
    if not response:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'No record with id: {id} found')
    return { "status" : status.HTTP_200_OK}

