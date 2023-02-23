from fastapi import APIRouter, HTTPException, status
from models.Marksheet import Marksheet,Marksheet_modify
from database.Marksheet_db import ( 
     addmarksheet,
     viewmarksheet,
     modifymarksheet,
     deletemarksheetid,
     searchmarksheet
)

router = APIRouter(
    prefix="/marksheet",
    tags=["Marksheet"],
    # dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},)

@router.get("/" )
async def view_marksheet():
    response = await viewmarksheet()
    if response: 
        return {
            "status " : status.HTTP_200_OK, 
            "marksheet list" : response }
    return {"error": status.HTTP_204_NO_CONTENT} 


# @router.get("/{marksheet_id}")
# async def search_marksheet(marksheet_id:str):
#     # print(marksheet_id)
#     response = await searchmarksheet(marksheet_id)
#     return response



@router.post("/")
async def create_marksheet(marksheet : Marksheet):
    response = await addmarksheet(marksheet.dict())
    if response==True:
        return {"response ": "Successfully added . . .",
            "status" : status.HTTP_200_OK}       
    return {"response" : response, "status" :status.HTTP_203_NON_AUTHORITATIVE_INFORMATION }


@router.put("/modify/{marksheet_id}")
async def modify_marksheet(marksheet_id: str , data : Marksheet_modify):
    response = await modifymarksheet(marksheet_id, data.dict(exclude_none=True))
    return response


@router.delete('/{id}')
async def delete_id(id: str):
    
    response = await deletemarksheetid(id)
    if not response:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'No record with id: {id} found')
    return { "Status":"Succesfully deleted ",
        "status_code " : status.HTTP_200_OK}





