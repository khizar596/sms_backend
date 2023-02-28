from fastapi import APIRouter, HTTPException, status
from models.Staff2 import Staff2 , Staff2_modify
from database.Staff2_db import ( 
    viewStaff2,
    deleteStaff2id,
    modifyStaff2,
    searchStaff2,
    addStaff2

)


router = APIRouter(
    prefix="/Staff2",
    tags=["Staff2"],
    # dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},)


router = APIRouter(
    prefix="/Staff2",
    tags=["Staff2"],
    # dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},)


@router.get("/")
async def view_Staff2():
    response = await viewStaff2()
    print(response)
    if response: 
        return {
            "status " : status.HTTP_200_OK, 
            "Staff2 list" : response }
    return {"error": status.HTTP_204_NO_CONTENT} 


@router.get("/{Staff2_id}")
async def search_Staff2(Staff2_id:str):
    # print(Staff2_id)
    response = await searchStaff2(Staff2_id)
    return response



@router.post("/")
async def enroll_Staff2(Staff2 : Staff2):
    
    response = await addStaff2(Staff2.dict())
    if response==True:
        return {"response ": "Successfully created . . .",
            "status" : status.HTTP_200_OK}       
    return {"response" : response, "status" :status.HTTP_203_NON_AUTHORITATIVE_INFORMATION }


@router.put("/modify/{Staff2_id}")
async def modify_Staff2(Staff2_id: str , data :Staff2_modify ):
    response = await modifyStaff2(Staff2_id, data.dict(exclude_none=True))
    return response


@router.delete('/{id}')
async def delete_id(id: str):
    
    response = await deleteStaff2id(id)
    if not response:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'No record with id: {id} found')
    return { "status " : status.HTTP_200_OK}

