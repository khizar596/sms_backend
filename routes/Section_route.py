from fastapi import APIRouter, HTTPException, status,Depends
from database.Section_db import( 
    addSection,
    viewSection,
    modifySection,
    deleteSectionid
)
from models.Section import Section, Section_modify
from database.auth import AuthHandler
auth_handler=AuthHandler()

router = APIRouter(
    prefix="/section",
    tags=["section"],
    dependencies=[Depends(auth_handler.auth_wrapper)],
    responses={404: {"description": "Not found"}},)

@router.get("/" )
async def view_Section(user=Depends(auth_handler.auth_wrapper)):
    auth_handler.has_permission(user, 'view_employee')

    response = await viewSection()
    if response: 
        return {
            "status " : status.HTTP_200_OK, 
            "Section list" : response }
    return {"error": status.HTTP_204_NO_CONTENT} 


# @router.get("/{Section_id}")
# async def search_Section(Section_id:str):
#     # print(Section_id)
#     response = await searchSection(Section_id)
#     return response



@router.post("/")
async def add_Section(Section : Section):
    response = await addSection(Section.dict())
    if response==True:
        return {"response ": "Successfully added . . .",
            "status" : status.HTTP_200_OK}       
    return {"response" : response, "status" :status.HTTP_203_NON_AUTHORITATIVE_INFORMATION }


@router.put("/modify/{Section_id}")
async def modify_Section(Section_id: str , data :Section_modify ):
    response = await modifySection(Section_id, data.dict(exclude_none=True))
    return response


@router.delete('/{id}')
async def delete_id(id: str):
    
    response = await deleteSectionid(id)
    if not response:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'No record with id: {id} found')
    return { "Status":"Succesfully deleted ",
        "status_code " : status.HTTP_200_OK}
