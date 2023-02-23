from fastapi import APIRouter, HTTPException, status
from models.Class_subject import Class_subject, Class_subject_modify
from database.Classsubject_db import ( 
    viewClasssubject,
    deleteclasssubjectid, 
    modifyClasssubject,
    searchClasssubject,
    addClasssubject

)


router = APIRouter(
    prefix="/classsubject",
    tags=["Class Subject"],
    # dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},)


@router.get("/" )
async def view_Classsubject():
    response = await viewClasssubject()
    if response: 
        return {
            "status " : status.HTTP_200_OK, 
            "Classsubject list" : response }
    return {"error": status.HTTP_204_NO_CONTENT} 


@router.get("/{Classsubject_id}")
async def search_Classsubject(Classsubject_id:str):
    # print(Classsubject_id)
    response = await searchClasssubject(Classsubject_id)
    return response



@router.post("/")
async def create_Classsubject(Classsubject : Class_subject):
    response = await addClasssubject(Classsubject.dict())
    if response==True:
        return {"response ": "Successfully added . . .",
            "status" : status.HTTP_200_OK}       
    return {"response" : response, "status" :status.HTTP_203_NON_AUTHORITATIVE_INFORMATION }


@router.put("/modify/{Classsubject_id}")
async def modify_Classsubject(Classsubject_id: str , data :Class_subject_modify ):
    response = await modifyClasssubject(Classsubject_id, data.dict(exclude_none=True))
    return response


@router.delete('/{id}')
async def delete_id(id: str):
    
    response = await deleteclasssubjectid(id)
    if not response:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'No record with id: {id} found')
    return { "Status":"Succesfully deleted ",
        "status_code " : status.HTTP_200_OK}

