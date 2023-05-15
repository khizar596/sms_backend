from fastapi import APIRouter, HTTPException,status,Depends
from fastapi import UploadFile
from models.Employee2 import Employee2, Employee2_modify
from database.Employee_db import (
    enrollemployee,
    modifyemployee,
    viewemployee, 
    searchemployee,
    deletebyid
)


from database.auth import AuthHandler
auth_handler=AuthHandler()

router = APIRouter(
    prefix="/employee",
    tags=["Employee"],
    dependencies=[Depends(auth_handler.auth_wrapper)],
    responses={404: {"description": "Not found"}})


@router.get("/")
async def view_employee(user = Depends(auth_handler.auth_wrapper)):
    auth_handler.has_permission(user, 'view_employee')
    
    response = await viewemployee()
    if response: 
        return {
            "status" : status.HTTP_200_OK, 
            "employeelist" : response }
    return {"error": status.HTTP_204_NO_CONTENT} 


@router.get("/{employee_id}")
async def search_employee(employee_id:str,user = Depends(auth_handler.auth_wrapper)):
    # print(employee_id)
    auth_handler.has_permission(user, 'view_employee')

    response = await searchemployee(employee_id)
    return response



@router.post("/")
async def enroll_employee(employee : Employee2,user = Depends(auth_handler.auth_wrapper)):
    
    response = await enrollemployee(employee.dict())
    if response==True:
        return {"response ": "Successfully created . . .",
            "status" : status.HTTP_200_OK}       
    return {"response" : response, "status" :status.HTTP_203_NON_AUTHORITATIVE_INFORMATION }


@router.put("/modify/{employee_id}")
async def modify_employee(employee_id: str , data :Employee2_modify ):
    response = await modifyemployee(employee_id, data.dict(exclude_none=True))
    return response


@router.delete('/{id}')
async def delete_id(id: str):
    
    response = await deletebyid(id)
    if not response:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'No record with id: {id} found')
    return { "status " : status.HTTP_200_OK}



