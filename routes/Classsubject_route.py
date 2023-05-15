from fastapi import APIRouter, HTTPException, status,Depends
from models.Class_subject import Class_subject, Class_subject_modify
from database.Classsubject_db import ( 
    viewClasssubject,
    deleteclasssubjectid, 
    modifyClasssubject,
    searchClasssubject,
    addClasssubject

)
from database.auth import AuthHandler
auth_handler=AuthHandler()


router = APIRouter(
    prefix="/classsubject",
    tags=["Class Subject"],
    dependencies=[Depends(auth_handler.auth_wrapper)],
    responses={404: {"description": "Not found"}},)


@router.get("/" )
async def view_Classsubject(user=Depends(auth_handler.auth_wrapper)):
    auth_handler.has_permission(user, 'view_subject')

    response = await viewClasssubject()
    if response: 
        return {
            "status" : status.HTTP_200_OK, 
            "Classsubjects" : response }
    return {"error": status.HTTP_204_NO_CONTENT} 


@router.get("/{Classsubject_id}")
async def search_Classsubject(Classsubject_id:str,user=Depends(auth_handler.auth_wrapper)):
    auth_handler.has_permission(user, 'search_subject')
    response = await searchClasssubject(Classsubject_id)
    return response



@router.post("/")
async def create_Classsubject(Classsubject : Class_subject,user=Depends(auth_handler.auth_wrapper)):
    auth_handler.has_permission(user, 'add_subject')
    response = await addClasssubject(Classsubject.dict())
    if response==True:
        return {"response ": "Successfully added . . .",
            "status" : status.HTTP_200_OK}       
    return {"response" : response, "status" :status.HTTP_203_NON_AUTHORITATIVE_INFORMATION }


@router.put("/modify/{Classsubject_id}",)

async def modify_Classsubject(Classsubject_id: str , data :Class_subject_modify ,user=Depends(auth_handler.auth_wrapper)):
    auth_handler.has_permission(user, 'modify_subject')

    response = await modifyClasssubject(Classsubject_id, data.dict(exclude_none=True))
    return response


@router.delete('/{id}')
async def delete_id(id: str,user=Depends(auth_handler.auth_wrapper)):
    auth_handler.has_permission(user, 'delete_employee')
    response = await deleteclasssubjectid(id)
    if not response:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'No record with id: {id} found')
    return { "Status":"Succesfully deleted ",
        "status_code " : status.HTTP_200_OK}

