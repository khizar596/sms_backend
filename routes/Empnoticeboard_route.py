from fastapi import APIRouter, HTTPException, status
from database.Empnoticeboard2_db import( 
    addempnotice,
    viewempnotice,
    modifyempnotice,
    deleteempnoticeid
)
from models.EmployeeNoticeboard2 import Emp_noticeboard_modify, Emp_noticeboard

router = APIRouter(
    prefix="/empnotice",
    tags=["Employee Notice Board"],
    # dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},)

@router.get("/" )
async def view_empnotice():
    response = await viewempnotice()
    if response: 
        return {
            "status " : status.HTTP_200_OK, 
            "empnotice list" : response }
    return {"error": status.HTTP_204_NO_CONTENT} 


# @router.get("/{empnotice_id}")
# async def search_empnotice(empnotice_id:str):
#     # print(empnotice_id)
#     response = await searchempnotice(empnotice_id)
#     return response



@router.post("/")
async def add_empnotice(empnotice : Emp_noticeboard):
    response = await addempnotice(empnotice.dict())
    if response==True:
        return {"response ": "Successfully added . . .",
            "status" : status.HTTP_200_OK}       
    return {"response" : response, "status" :status.HTTP_203_NON_AUTHORITATIVE_INFORMATION }


@router.put("/modify/{empnotice_id}")
async def modify_empnotice(empnotice_id: str , data :Emp_noticeboard_modify ):
    response = await modifyempnotice(empnotice_id, data.dict(exclude_none=True))
    return response


@router.delete('/{id}')
async def delete_id(id: str):
    
    response = await deleteempnoticeid(id)
    if not response:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'No record with id: {id} found')
    return { "Status":"Succesfully deleted ",
        "status_code " : status.HTTP_200_OK}
