from fastapi import APIRouter, HTTPException, status,Depends
from database.Stdnoticeboatd_db import( 
    addstdnotice,
    viewstdnotice,
    modifystdnotice,
    deletestdnoticeid
)
from models.StudentNoticeboard import StudentNoticeboard, StudentNoticeboard_modify
from database.auth import AuthHandler
auth_handler=AuthHandler()

router = APIRouter(
    prefix="/stdnotice",
    tags=["Student Notice Board"],
    dependencies=[Depends(auth_handler.auth_wrapper)],
    responses={404: {"description": "Not found"}},)

@router.get("/" )
async def view_stdnotice(user=Depends(auth_handler.auth_wrapper)):
    auth_handler.has_permission(user, 'view_employee')

    response = await viewstdnotice()
    if response: 
        return {
            "status" : status.HTTP_200_OK, 
            "stdnotices" : response }
    return {"error": status.HTTP_204_NO_CONTENT} 


# @router.get("/{stdnotice_id}")
# async def search_stdnotice(stdnotice_id:str):
#     # print(stdnotice_id)
#     response = await searchstdnotice(stdnotice_id)
#     return response



@router.post("/")
async def add_stdnotice(stdnotice : StudentNoticeboard):
    response = await addstdnotice(stdnotice.dict())
    if response==True:
        return {"response ": "Successfully added . . .",
            "status" : status.HTTP_200_OK}       
    return {"response" : response, "status" :status.HTTP_203_NON_AUTHORITATIVE_INFORMATION }


@router.put("/modify/{stdnotice_id}")
async def modify_stdnotice(stdnotice_id: str , data :StudentNoticeboard_modify ):
    response = await modifystdnotice(stdnotice_id, data.dict(exclude_none=True))
    return response


@router.delete('/{id}')
async def delete_id(id: str):
    
    response = await deletestdnoticeid(id)
    if not response:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'No record with id: {id} found')
    return { "Status":"Succesfully deleted ",
        "status_code " : status.HTTP_200_OK}
