from fastapi import APIRouter,status, HTTPException
from models.Parent import Parent , Parent_modify
from database.Parents_db import (
    addparent,
    modifyparent,
    viewparent, 
    searchparent,
    deletebyid
)



router = APIRouter(
    prefix="/parent",
    tags=["Parent"],
    # dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},)

@router.get("/" )
async def view_parent():
    response = await viewparent()
    print(response)
    if response: 
        return {
            "status " : status.HTTP_200_OK, 
            "parent list" : response }
    return {"error": status.HTTP_204_NO_CONTENT} 


@router.get("/{parent_id}")
async def search_parent(parent_id:str):
    # print(parent_id)
    response = await searchparent(parent_id)
    return response



@router.post("/")
async def add_parent(parent : Parent):
    
    response = await addparent(parent.dict())
    if response==True:
        return {"response ": "Successfully created . . .",
            "status" : status.HTTP_200_OK}       
    return {"response" : response, "status" :status.HTTP_203_NON_AUTHORITATIVE_INFORMATION }


@router.put("/modify/{parent_id}")
async def modify_parent(parent_id: str , data :Parent_modify ):
    response = await modifyparent(parent_id, data.dict(exclude_none=True))
    return response


@router.delete('/{id}')
async def delete_id(id: str):
    
    response = await deletebyid(id)
    if not response:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'No record with id: {id} found')
    return { "status " : status.HTTP_200_OK}