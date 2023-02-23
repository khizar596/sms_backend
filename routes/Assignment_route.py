from fastapi import APIRouter, HTTPException , status
from models.Assignment import Assignment, Assignment_modify
from database.Assignment_db import (
    viewAssignment  , 
    modifyAssignment, 
    searchAssignment,
    deleteAssignmentid,
    addAssignment

)


router = APIRouter(
    prefix="/assignment",
    tags=["Assingment"],
    # dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},)


@router.get("/" )
async def view_Assignment():
    response = await viewAssignment()
    if response: 
        return {
            "status " : status.HTTP_200_OK, 
            "Assignment list" : response }
    return {"error": status.HTTP_204_NO_CONTENT} 


@router.get("/{Assignment_id}")
async def search_Assignment(Assignment_id:str):
    # print(Assignment_id)
    response = await searchAssignment(Assignment_id)
    return response



@router.post("/")
async def create_Assignment(Assignment : Assignment):
    response = await addAssignment(Assignment.dict())
    if response==True:
        return {"response ": "Successfully added . . .",
            "status" : status.HTTP_200_OK}       
    return {"response" : response, "status" :status.HTTP_203_NON_AUTHORITATIVE_INFORMATION }


@router.put("/modify/{Assignment_id}")
async def modify_Assignment(Assignment_id: str , data : Assignment_modify):
    response = await modifyAssignment(Assignment_id, data.dict(exclude_none=True))
    return response


@router.delete('/{id}')
async def delete_id(id: str):
    
    response = await deleteAssignmentid(id)
    if not response:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'No record with id: {id} found')
    return { "Status":"Succesfully deleted ",
        "status_code " : status.HTTP_200_OK}

