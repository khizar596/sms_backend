from fastapi import APIRouter,status, HTTPException,Depends
from database.Class_db import (
    addClass,
    viewClass,
    modifyClass,searchClass,
    deleteclassid
)
from models.Class import Class,Class_modify
from database.auth import AuthHandler
auth_handler=AuthHandler()

router = APIRouter(
    prefix="/class",
    tags=["Class"],
    dependencies=[Depends(auth_handler.auth_wrapper)],
    responses={404: {"description": "Not found"}},)

@router.get("/" )
async def view_Class(user=Depends(auth_handler.auth_wrapper)):
    auth_handler.has_permission(user, 'view_class')

    response = await viewClass()
    if response: 
        return {
            "status" : status.HTTP_200_OK, 
            "Classlist" : response }
    return {"error": status.HTTP_204_NO_CONTENT} 


@router.get("/{Class_id}")
async def search_Class(Class_id:str,user=Depends(auth_handler.auth_wrapper)):
    auth_handler.has_permission(user, 'search_class')
    response = await searchClass(Class_id)
    return response



@router.post("/")
async def create_Class(Class : Class,user=Depends(auth_handler.auth_wrapper)):
    response = await addClass(Class.dict())
    auth_handler.has_permission(user, 'add_class')

    if response==True:
        return {"response ": "Successfully added . . .",
            "status" : status.HTTP_200_OK}       
    return {"response" : response, "status" :status.HTTP_203_NON_AUTHORITATIVE_INFORMATION }


@router.put("/modify/{Class_id}")
async def modify_Class(Class_id: str , data :Class_modify ,user=Depends(auth_handler.auth_wrapper)):
    auth_handler.has_permission(user, 'modify_class')

    response = await modifyClass(Class_id, data.dict(exclude_none=True))
    return response


@router.delete('/{id}')
async def delete_id(id: str,user=Depends(auth_handler.auth_wrapper)):
    auth_handler.has_permission(user, 'delete_class')

    response = await deleteclassid(id)
    if not response:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'No record with id: {id} found')
    return { "Status":"Succesfully deleted ",
        "status_code " : status.HTTP_200_OK}
