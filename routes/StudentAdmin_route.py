from fastapi import APIRouter, HTTPException, status
from models.StudentAdmin import StudentAdmin , StudentAdmin_modify
from database.StudentAdmin_db import ( 
    viewStudentAdmin,
    deleteStudentAdminid,
    modifyStudentAdmin,
    searchStudentAdmin,
    addStudentAdmin

)


router = APIRouter(
    prefix="/StudentAdmin",
    tags=["StudentAdmin"],
    # dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},)


router = APIRouter(
    prefix="/StudentAdmin",
    tags=["StudentAdmin"],
    # dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},)


@router.get("/")
async def view_StudentAdmin():
    response = await viewStudentAdmin()
    print(response)
    if response: 
        return {
            "status " : status.HTTP_200_OK, 
            "StudentAdmin list" : response }
    return {"error": status.HTTP_204_NO_CONTENT} 


@router.get("/{StudentAdmin_id}")
async def search_StudentAdmin(StudentAdmin_id:str):
    # print(StudentAdmin_id)
    response = await searchStudentAdmin(StudentAdmin_id)
    return response



@router.post("/")
async def enroll_StudentAdmin(StudentAdmin : StudentAdmin):
    
    response = await addStudentAdmin(StudentAdmin.dict())
    if response==True:
        return {"response ": "Successfully created . . .",
            "status" : status.HTTP_200_OK}       
    return {"response" : response, "status" :status.HTTP_203_NON_AUTHORITATIVE_INFORMATION }


@router.put("/modify/{StudentAdmin_id}")
async def modify_StudentAdmin(StudentAdmin_id: str , data :StudentAdmin_modify ):
    response = await modifyStudentAdmin(StudentAdmin_id, data.dict(exclude_none=True))
    return response


@router.delete('/{id}')
async def delete_id(id: str):
    
    response = await deleteStudentAdminid(id)
    if not response:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'No record with id: {id} found')
    return { "status " : status.HTTP_200_OK}

