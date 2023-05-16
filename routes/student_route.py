from fastapi import APIRouter, UploadFile,File,HTTPException,Depends ,status,Form
from typing import Optional,List
from pydantic import EmailStr 

from models.Student import Student, Student_modify
from database.auth import AuthHandler
from fastapi.responses import FileResponse
import os
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





@router.put("/modify/{student_id}")
async def modify_student(student_id: str,
                         first_name: Optional[str] = Form(None),
                         last_name: Optional[str] = Form(None),
                         parent_name: Optional[str] = Form(None),
                         password: Optional[str] = Form(None),
                         cnic: Optional[str] = Form(None),
                         address: Optional[str] = Form(None),
                         gender: Optional[str] = Form(None),
                         dob: Optional[str] = Form(None),
                         email: Optional[EmailStr] = Form(None),
                         image: Optional[UploadFile] = File(None),
                         phone: Optional[int] = Form(None),
                         blood_group: Optional[str] = Form(None),
                         religion: Optional[str] = Form(None),
                         previous_school: Optional[str] = Form(None),
                         session: Optional[str] = Form(None),
                         class_id: Optional[str] = Form(None),
                         role: Optional[List[str]] = Form([]),
                         blocked: Optional[bool] = Form(False),
                         user=Depends(auth_handler.auth_wrapper)):
    auth_handler.has_permission(user, 'modify_student')

    data = {
        'first_name': first_name,
        'last_name': last_name,
        'parent_name': parent_name,
        'password': password,
        'cnic': cnic,
        'address': address,
        'gender': gender,
        'dob': dob,
        'email': email,
        'phone': phone,
        'blood_group': blood_group,
        'religion': religion,
        'previous_school': previous_school,
        'session': session,
        'class_id': class_id,
        'role': role,
        'blocked': blocked
    }

    filtered_data = {key: value for key, value in data.items() if value is not None}

    response = await modifystudent(student_id, filtered_data, image)
    return response

@router.delete('/{id}')
async def delete_id(id: str,user = Depends(auth_handler.auth_wrapper)):
    auth_handler.has_permission(user, 'delete_student')

    response = await deletebyid(id)
    if not response:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'No record with id: {id} found')
    return { "status" : status.HTTP_200_OK}




# ************************************IMAGE INSERTION***************************************************

@router.get('/profile_pics/{filename}')
async def get_image(filename: str):
    UPLOAD_profilepic = 'profile_pics'

    file_path = os.path.join(UPLOAD_profilepic, filename)
    return FileResponse(file_path)




@router.post("/")
async def enroll_student(
    first_name: str = Form(...),
    last_name: str = Form(...),
    parent_name: str = Form(...),
    password: str = Form(...),
    cnic: str = Form(...),
    address: str = Form(...),
    gender: str = Form(...),
    dob: str = Form(...),
    email: EmailStr = Form(...),
    image: UploadFile = File(None),
    phone: int = Form(...),
    blood_group: str = Form(...),
    religion: str = Form(...),
    previous_school: str = Form(...),
    session: str = Form(...),
    class_id: str = Form(...),
    role: List[str] = Form([]),
    blocked: Optional[bool] = Form(False),
    user = Depends(auth_handler.auth_wrapper)):
    auth_handler.has_permission(user, 'add_student')
    student = Student(
        first_name=first_name,
        last_name=last_name,
        parent_name=parent_name,
        password=password,
        cnic=cnic,
        address=address,
        gender=gender,
        dob=dob,
        email=email,
        image='',
        phone=phone,
        blood_group=blood_group,
        religion=religion,
        previous_school=previous_school,
        session=session,
        class_id=class_id,
        role=role,
        blocked=blocked
    )
    response = await enrollstudent(student.dict(exclude_none=True),image)
    if response==True:
        return {"response ": "Successfully created . . .",
            "status" : status.HTTP_200_OK}       
    return {"response" : response, "status" :status.HTTP_203_NON_AUTHORITATIVE_INFORMATION }