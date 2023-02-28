from fastapi import APIRouter, HTTPException, status
from models.Teacher import Teacher , Teacher_modify
from database.Teacher_db import ( 
    viewTeacher,
    deleteTeacherid,
    modifyTeacher,
    searchTeacher,
    addTeacher

)


router = APIRouter(
    prefix="/Teacher",
    tags=["Teacher"],
    # dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},)


router = APIRouter(
    prefix="/Teacher",
    tags=["Teacher"],
    # dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},)


@router.get("/")
async def view_Teacher():
    response = await viewTeacher()
    print(response)
    if response: 
        return {
            "status " : status.HTTP_200_OK, 
            "Teacher list" : response }
    return {"error": status.HTTP_204_NO_CONTENT} 


@router.get("/{Teacher_id}")
async def search_Teacher(Teacher_id:str):
    # print(Teacher_id)
    response = await searchTeacher(Teacher_id)
    return response



@router.post("/")
async def enroll_Teacher(Teacher : Teacher):
    
    response = await addTeacher(Teacher.dict())
    if response==True:
        return {"response ": "Successfully created . . .",
            "status" : status.HTTP_200_OK}       
    return {"response" : response, "status" :status.HTTP_203_NON_AUTHORITATIVE_INFORMATION }


@router.put("/modify/{Teacher_id}")
async def modify_Teacher(Teacher_id: str , data :Teacher_modify ):
    response = await modifyTeacher(Teacher_id, data.dict(exclude_none=True))
    return response


@router.delete('/{id}')
async def delete_id(id: str):
    
    response = await deleteTeacherid(id)
    if not response:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'No record with id: {id} found')
    return { "status " : status.HTTP_200_OK}

