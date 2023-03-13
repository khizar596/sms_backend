from fastapi import APIRouter, HTTPException, status,Depends
from models.Employee_role import EmployeeRole , Employeerole_modify, Role
from database.Employee_role_db import ( 
    viewEmployee_role,
    deleteEmployee_roleid,
    modifyEmployee_role,
    searchEmployee_role,
    addEmployee_role

)
from database.auth import AuthHandler
auth_handler=AuthHandler()


router = APIRouter(
    prefix="/Employee_role",
    tags=["Employee_role"],
    dependencies=[Depends(auth_handler.auth_wrapper)],
    responses={404: {"description": "Not found"}},)



@router.get("/")
async def view_Employee_role(user=Depends(auth_handler.auth_wrapper)):
    auth_handler.has_permission(user, 'view_employee')

    response = await viewEmployee_role()
    if response: 
        return {
            "status " : status.HTTP_200_OK, 
            "Employee_role list" : response }
    return {"error": status.HTTP_204_NO_CONTENT} 


@router.get("/{Employee_role_id}")
async def search_Employee_role(Employee_role_id:str):
    # print(Employee_role_id)
    response = await searchEmployee_role(Employee_role_id)
    return response



@router.post("/")
async def enroll_Employee_role(Employee_role : Role):
    
    response = await addEmployee_role(Employee_role.dict())
    if response==True:
        return {"response ": "Successfully created . . .",
            "status" : status.HTTP_200_OK}       
    return {"response" : response, "status" :status.HTTP_203_NON_AUTHORITATIVE_INFORMATION }


@router.put("/modify/{Employee_role_id}")
async def modify_Employee_role(Employee_role_id: str , data :Employeerole_modify ):
    response = await modifyEmployee_role(Employee_role_id, data.dict(exclude_none=True))
    return response


@router.delete('/{id}')
async def delete_id(id: str):
    
    response = await deleteEmployee_roleid(id)
    if not response:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'No record with id: {id} found')
    return { "status " : status.HTTP_200_OK}

