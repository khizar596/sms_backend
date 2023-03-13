from fastapi import APIRouter, HTTPException , status,Depends
from models.Assignment import Assignment, Assignment_modify
from database.Assignment_db import (
    viewAssignment  , 
    modifyAssignment, 
    searchAssignment,
    deleteAssignmentid,
    addAssignment

)
from database.auth import AuthHandler
auth_handler=AuthHandler()


router = APIRouter(
    prefix="/assignment",
    tags=["Assingment"],
    dependencies=[Depends(auth_handler.auth_wrapper)],
    responses={404: {"description": "Not found"}},)


@router.get("/" )
async def view_Assignment(user=Depends(auth_handler.auth_wrapper)):
    auth_handler.has_permission(user, 'view_assignment')

    response = await viewAssignment()
    if response: 
        return {
            "status " : status.HTTP_200_OK, 
            "Assignment list" : response }
    return {"error": status.HTTP_204_NO_CONTENT} 


@router.get("/{Assignment_id}")
async def search_Assignment(Assignment_id:str,user=Depends(auth_handler.auth_wrapper)):
    auth_handler.has_permission(user, 'search_assignment')
    response = await searchAssignment(Assignment_id)
    return response



@router.post("/")
async def create_Assignment(Assignment : Assignment,user=Depends(auth_handler.auth_wrapper)):
    response = await addAssignment(Assignment.dict())
    auth_handler.has_permission(user, 'add_assignment')

    
    if response==True:
        return {"response ": "Successfully added . . .",
            "status" : status.HTTP_200_OK}       
    return {"response" : response, "status" :status.HTTP_203_NON_AUTHORITATIVE_INFORMATION }


@router.put("/modify/{Assignment_id}")
async def modify_Assignment(Assignment_id: str , data : Assignment_modify,user=Depends(auth_handler.auth_wrapper)):
    auth_handler.has_permission(user, 'modify_assignment')

    response = await modifyAssignment(Assignment_id, data.dict(exclude_none=True))
    return response


@router.delete('/{id}')
async def delete_id(id: str,user=Depends(auth_handler.auth_wrapper)):
    
    response = await deleteAssignmentid(id,)
    auth_handler.has_permission(user, 'delete_assignment')

    if not response:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'No record with id: {id} found')
    return { "Status":"Succesfully deleted ",
        "status_code " : status.HTTP_200_OK}

