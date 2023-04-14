from fastapi import APIRouter, HTTPException  , status,Depends
from database.employeecomplain_db import ( 
    viewEmp_comp,
    addEmp_comp,
    modifyEmp_comp,
    deletebyid
)
from models.EmployeeComplain import EmployeeComplain,EmployeeComplain_modify
from database.auth import AuthHandler
auth_handler=AuthHandler()

router = APIRouter(
    prefix="/empcomplain",
    tags=["Employee Complain"],
    dependencies=[Depends(auth_handler.auth_wrapper)],
    responses={404: {"description": "Not found"}})


@router.get("/" )
async def view_Emp_comp(user=Depends(auth_handler.auth_wrapper)):
    auth_handler.has_permission(user, 'view_employee')

    response = await viewEmp_comp()
    if response: 
        return {
            "status " : status.HTTP_200_OK, 
            "Emp_comp list" : response }
    return {"error": status.HTTP_204_NO_CONTENT} 


# @router.get("/{Emp_comp_id}")
# async def search_Emp_comp(Emp_comp_id:str):
#     # print(Emp_comp_id)
#     response = await searchEmp_comp(Emp_comp_id)
#     return response



@router.post("/")
async def create_Emp_comp(Emp_comp : EmployeeComplain):
    response = await addEmp_comp(Emp_comp.dict(exclude_none=False))
    if response==True:
        return {"response ": "Successfully created . . .",
            "status" : status.HTTP_200_OK}       
    return {"response" : response, "status" :status.HTTP_203_NON_AUTHORITATIVE_INFORMATION }


@router.put("/modify/{Emp_comp_id}")
async def modify_Emp_comp(Emp_comp_id: str , data :EmployeeComplain_modify ):
    response = await modifyEmp_comp(Emp_comp_id, data.dict(exclude_none=True))
    return response


@router.delete('/{id}')
async def delete_id(id: str):
    
    response = await deletebyid(id)
    if not response:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'No record with id: {id} found')
    return { "Status":"Succesfully deleted ",
        "status_code " : status.HTTP_200_OK}





# if item_id not in fake_items_db:
#     raise HTTPException(status_code=404, detail="Item not found")
# return {"name": fake_items_db[item_id]["name"], "item_id": item_id}
