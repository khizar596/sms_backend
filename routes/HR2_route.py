from fastapi import APIRouter, HTTPException, status,Depends
from models.HR2 import HR2 , HR2_modify
from database.HR2_db import ( 
    viewHR2,
    deleteHR2id,
    modifyHR2,
    searchHR2,
    addHR2

)
from database.auth import AuthHandler
auth_handler=AuthHandler()


router = APIRouter(
    prefix="/HR2",
    tags=["HR2"],
    dependencies=[Depends(auth_handler.auth_wrapper)],
    responses={404: {"description": "Not found"}},)


@router.get("/")
async def view_HR2(user=Depends(auth_handler.auth_wrapper)):
    auth_handler.has_permission(user, 'view_employee')

    response = await viewHR2()
    print(response)
    if response: 
        return {
            "status " : status.HTTP_200_OK, 
            "HR2 list" : response }
    return {"error": status.HTTP_204_NO_CONTENT} 


@router.get("/{HR2_id}")
async def search_HR2(HR2_id:str):
    # print(HR2_id)
    response = await searchHR2(HR2_id)
    return response



@router.post("/")
async def enroll_HR2(HR2 : HR2):
    
    response = await addHR2(HR2.dict())
    if response==True:
        return {"response ": "Successfully created . . .",
            "status" : status.HTTP_200_OK}       
    return {"response" : response, "status" :status.HTTP_203_NON_AUTHORITATIVE_INFORMATION }


@router.put("/modify/{HR2_id}")
async def modify_HR2(HR2_id: str , data :HR2_modify ):
    response = await modifyHR2(HR2_id, data.dict(exclude_none=True))
    return response


@router.delete('/{id}')
async def delete_id(id: str):
    
    response = await deleteHR2id(id)
    if not response:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'No record with id: {id} found')
    return { "status " : status.HTTP_200_OK}

