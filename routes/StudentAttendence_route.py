from fastapi import APIRouter, HTTPException, status,Depends
from database.StudentAttendence_db import ( 
     addSTD_attendence,
     viewSTD_attendence,
     modifySTD_attendence,
     searchSTD_attendence,
     deleteSTD_attendenceid
)
from models.StudentAttendence import StudentAttendence,StudentAttendence_modify
from database.auth import AuthHandler
auth_handler=AuthHandler()

router = APIRouter(
    prefix="/stdattendence",
    tags=["Student_attendence"],
    dependencies=[Depends(auth_handler.auth_wrapper)],
    responses={404: {"description": "Not found"}},)


@router.get("/" )
async def view_STD_attendence(user=Depends(auth_handler.auth_wrapper)):
    auth_handler.has_permission(user, 'view_employee')

    response = await viewSTD_attendence()
    if response: 
        return {
            "status" : status.HTTP_200_OK, 
            "STD_attendences" : response }
    return {"error": status.HTTP_204_NO_CONTENT} 


@router.get("/{STD_attendence_id}")
async def search_STD_attendence(STD_attendence_id:str):
    # print(STD_attendence_id)
    response = await searchSTD_attendence(STD_attendence_id)
    return response



@router.post("/")
async def mark_STD_attendence(STD_attendence : StudentAttendence):
    response = await addSTD_attendence(STD_attendence.dict())
    if response==True:
        return {"response ": "Successfully added . . .",
            "status" : status.HTTP_200_OK}       
    return {"response" : response, "status" :status.HTTP_203_NON_AUTHORITATIVE_INFORMATION }


@router.put("/modify/{STD_attendence_id}")
async def modify_STD_attendence(STD_attendence_id: str , data : StudentAttendence_modify):
    response = await modifySTD_attendence(STD_attendence_id, data.dict(exclude_none=True))
    return response


@router.delete('/{id}')
async def delete_std_id(id: str):
    
    response = await deleteSTD_attendenceid(id)
    if not response:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'No record with id: {id} found')
    return { "Status":"Succesfully deleted ",
        "status_code " : status.HTTP_200_OK}




