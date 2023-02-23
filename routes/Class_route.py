from fastapi import APIRouter,status, HTTPException
from database.Class_db import (
    addClass,
    viewClass,
    modifyClass,
    deleteclassid
)
from models.Class import Class,Class_modify

router = APIRouter(
    prefix="/class",
    tags=["Class"],
    # dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},)

@router.get("/" )
async def view_Class():
    response = await viewClass()
    if response: 
        return {
            "status " : status.HTTP_200_OK, 
            "Class list" : response }
    return {"error": status.HTTP_204_NO_CONTENT} 


# @router.get("/{Class_id}")
# async def search_Class(Class_id:str):
#     # print(Class_id)
#     response = await searchClass(Class_id)
#     return response



@router.post("/")
async def create_Class(Class : Class):
    response = await addClass(Class.dict())
    if response==True:
        return {"response ": "Successfully added . . .",
            "status" : status.HTTP_200_OK}       
    return {"response" : response, "status" :status.HTTP_203_NON_AUTHORITATIVE_INFORMATION }


@router.put("/modify/{Class_id}")
async def modify_Class(Class_id: str , data :Class_modify ):
    response = await modifyClass(Class_id, data.dict(exclude_none=True))
    return response


@router.delete('/{id}')
async def delete_id(id: str):
    
    response = await deleteclassid(id)
    if not response:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'No record with id: {id} found')
    return { "Status":"Succesfully deleted ",
        "status_code " : status.HTTP_200_OK}
