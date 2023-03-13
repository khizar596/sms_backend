from fastapi import APIRouter, HTTPException , status,Depends
from models.Courses import Courses_modify, Courses
from database.Courses_db import ( 
     viewCourse, 
      addCourse,
      modifyCourse,
      searchCourse,
      deleteCourseid
)
from database.auth import AuthHandler
auth_handler=AuthHandler()


router = APIRouter(
    prefix="/course",
    tags=["Courses"],
    dependencies=[Depends(auth_handler.auth_wrapper)],
    responses={404: {"description": "Not found"}})


@router.get("/" )
async def view_Course(user=Depends(auth_handler.auth_wrapper)):
    auth_handler.has_permission(user, 'view_employee')

    response = await viewCourse()
    if response: 
        return {
            "status " : status.HTTP_200_OK, 
            "Course list" : response }
    return {"error": status.HTTP_204_NO_CONTENT} 


@router.get("/{Course_id}")
async def search_Course(Course_id:str):
    # print(Course_id)
    response = await searchCourse(Course_id)
    return response



@router.post("/")
async def create_Course(Course : Courses):
    response = await addCourse(Course.dict())
    if response==True:
        return {"response ": "Successfully added . . .",
            "status" : status.HTTP_200_OK}       
    return {"response" : response, "status" :status.HTTP_203_NON_AUTHORITATIVE_INFORMATION }


@router.put("/modify/{Course_id}")
async def modify_Course(Course_id: str , data : Courses_modify):
    response = await modifyCourse(Course_id, data.dict(exclude_none=True))
    return response


@router.delete('/{id}')
async def delete_id(id: str):
    
    response = await deleteCourseid(id)
    if not response:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'No record with id: {id} found')
    return { "Status":"Succesfully deleted ",
        "status_code " : status.HTTP_200_OK}







