from fastapi import APIRouter, HTTPException, status,Depends
from database.Datesheet_db import ( 
     adddatesheet,
     viewdatesheet,
     modifydatesheet,
     deletedatesheetid,
     searchdatesheet
)
from models.Datesheet import Datesheet,Datesheet_modify

from database.auth import AuthHandler
auth_handler=AuthHandler()


router = APIRouter(
    prefix="/datesheet",
    tags=["Datesheet"],
    dependencies=[Depends(auth_handler.auth_wrapper)],
    responses={404: {"description": "Not found"}},)


@router.get("/" )
async def view_datesheet(user=Depends(auth_handler.auth_wrapper)):
    auth_handler.has_permission(user, 'view_datesheet')

    response = await viewdatesheet()
    if response: 
        return {
            "status" : status.HTTP_200_OK, 
            "datesheet list" : response }
    return {"error": status.HTTP_204_NO_CONTENT} 


@router.get("/{datesheet_id}")
async def search_datesheet(datesheet_id:str,user=Depends(auth_handler.auth_wrapper)):
    auth_handler.has_permission(user, 'search_datesheet')
    response = await searchdatesheet(datesheet_id)
    return response



@router.post("/")
async def create_datesheet(datesheet : Datesheet,user=Depends(auth_handler.auth_wrapper)):
    response = await adddatesheet(datesheet.dict())
    auth_handler.has_permission(user, 'add_datesheet')

    if response==True:
        return {"response ": "Successfully added . . .",
            "status" : status.HTTP_200_OK}       
    return {"response" : response, "status" :status.HTTP_203_NON_AUTHORITATIVE_INFORMATION }


@router.put("/modify/{datesheet_id}")
async def modify_datesheet(datesheet_id: str , data : Datesheet_modify,user=Depends(auth_handler.auth_wrapper)):
    auth_handler.has_permission(user, 'modify_datesheet')

    response = await modifydatesheet(datesheet_id, data.dict(exclude_none=True))
    return response


@router.delete('/{id}')
async def delete_id(id: str,user=Depends(auth_handler.auth_wrapper)):
    auth_handler.has_permission(user, 'delete_datesheet')
  
    response = await deletedatesheetid(id)
    if not response:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'No record with id: {id} found')
    return { "Status":"Succesfully deleted ",
        "status_code " : status.HTTP_200_OK}





