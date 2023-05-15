from fastapi import APIRouter, HTTPException,Depends ,status
from models.Student import Student, Student_modify
from database.auth import AuthHandler
auth_handler=AuthHandler()
from database.Student_db import (
    enrollstudent,
    modifystudent,
    viewStudent, 
    searchStudent,
    deletebyid
)


router = APIRouter(
    prefix="/student",
    tags=["Student"],
    # dependencies=[Depends(auth_handler.auth_wrapper)],
    responses={404: {"description": "Not found"}})

@router.get("/")
async def view_student():
    # auth_handler.has_permission(user, 'view_student')

    response = await viewStudent()
    if response: 
        return {
            "status" : status.HTTP_200_OK, 
            "Students" : response }
    return {"error": status.HTTP_204_NO_CONTENT} 


@router.get("/{student_id}")
async def search_student(student_id:str,user = Depends(auth_handler.auth_wrapper)):
    auth_handler.has_permission(user, 'search_student')

    # print(student_id)
    response = await searchStudent(student_id)
    return response



@router.post("/")
async def enroll_student(student : Student,user = Depends(auth_handler.auth_wrapper)):
    auth_handler.has_permission(user, 'add_student')

    response = await enrollstudent(student.dict())
    if response==True:
        return {"response ": "Successfully created . . .",
            "status" : status.HTTP_200_OK}       
    return {"response" : response, "status" :status.HTTP_203_NON_AUTHORITATIVE_INFORMATION }


@router.put("/modify/{student_id}")
async def modify_student(student_id: str , data :Student_modify):
    # auth_handler.has_permission(user, 'modify_student')

    response = await modifystudent(student_id, data.dict(exclude_none=True))
    return response


@router.delete('/{id}')
async def delete_id(id: str,user = Depends(auth_handler.auth_wrapper)):
    auth_handler.has_permission(user, 'delete_student')

    response = await deletebyid(id)
    if not response:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'No record with id: {id} found')
    return { "status" : status.HTTP_200_OK}



# if item_id not in fake_items_db:
#     raise HTTPException(status_code=404, detail="Item not found")
# return {"name": fake_items_db[item_id]["name"], "item_id": item_id}
