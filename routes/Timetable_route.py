from fastapi import APIRouter, HTTPException, status,Depends
from database.Timetable_db import ( 
     addtimetable,
     viewtimetable,
     modifytimetable,
     deletetimetableid,
     searchtimetable
)
from models.Timetable import Timetable,Timetable_modify
from database.auth import AuthHandler
auth_handler=AuthHandler()

router = APIRouter(
    prefix="/timetable",
    tags=["Timetable"],
    # dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},)

@router.get("/" )
async def view_timetable(user=Depends(auth_handler.auth_wrapper)):
    auth_handler.has_permission(user, 'view_employee')

    response = await viewtimetable()
    if response: 
        return {
            "status " : status.HTTP_200_OK, 
            "timetable list" : response }
    return {"error": status.HTTP_204_NO_CONTENT} 


# @router.get("/{timetable_id}")
# async def search_timetable(timetable_id:str):
#     # print(timetable_id)
#     response = await searchtimetable(timetable_id)
#     return response



@router.post("/")
async def create_timetable(timetable : Timetable):
    response = await addtimetable(timetable.dict())
    if response==True:
        return {"response ": "Successfully added . . .",
            "status" : status.HTTP_200_OK}       
    return {"response" : response, "status" :status.HTTP_203_NON_AUTHORITATIVE_INFORMATION }


@router.put("/modify/{timetable_id}")
async def modify_timetable(timetable_id: str , data : Timetable_modify):
    response = await modifytimetable(timetable_id, data.dict(exclude_none=True))
    return response


@router.delete('/{id}')
async def delete_id(id: str):
    
    response = await deletetimetableid(id)
    if not response:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'No record with id: {id} found')
    return { "Status":"Succesfully deleted ",
        "status_code " : status.HTTP_200_OK}






