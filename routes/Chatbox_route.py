from fastapi import APIRouter, HTTPException , status, WebSocket,Depends
from models.chatbox import Chatbox , Chatbox_modify
from fastapi.responses import JSONResponse

from database.Chatbox_db import (
    viewchatbox,
    addchatbox,
    deletechatboxid,
    modifychatbox

    # searchchatbox
)
from database.auth import AuthHandler
auth_handler=AuthHandler()

router = APIRouter(
    prefix="/chatbox",
    tags=["Chatbox"],
    dependencies=[Depends(auth_handler.auth_wrapper)],
    responses={404: {"description": "Not found"}})




@router.get("/" )
async def view_chatbox(user=Depends(auth_handler.auth_wrapper)):
    auth_handler.has_permission(user, 'view_employee')

    response = await viewchatbox()
    if response: 
        return {
            "status " : status.HTTP_200_OK, 
            "chatbox list" : response }
    return {"error": status.HTTP_204_NO_CONTENT} 


# @router.get("/{chatbox_id}")
# async def search_chatbox(chatbox_id:str):
#     # print(chatbox_id)
#     response = await searchchatbox(chatbox_id)
#     return response



@router.post("/")
async def create_chatbox(chatbox : Chatbox):
    response = await addchatbox(chatbox.dict())
    if response==True:
        return {"response ": "Successfully added . . .",
            "status" : status.HTTP_200_OK}       
    return {"response" : response, "status" :status.HTTP_203_NON_AUTHORITATIVE_INFORMATION }


@router.put("/modify/{chatbox_id}")
async def modify_chatbox(chatbox_id: str , data : Chatbox_modify):
    response = await modifychatbox(chatbox_id, data.dict(exclude_none=True))
    return response


@router.delete('/{id}')
async def delete_id(id: str):
    
    response = await deletechatboxid(id)
    if not response:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'No record with id: {id} found')
    return { "Status":"Succesfully deleted ",
        "status_code " : status.HTTP_200_OK}



# $$$$ WEBSOCKET  CHATTING LOGIC

