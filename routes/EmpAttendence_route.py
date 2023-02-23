from fastapi import APIRouter, HTTPException, status
from models.employeeattendance2 import employeeattendance2_modify,employeeattendance2
from database.EmpAttendence2_db import ( 
    viewEmp_Attendence2,
    # searchEmp_Attendence2,
    addEmp_Attendence2,
    deleteEmp_Attendence2id,
    modifyEmp_Attendence2
)


router = APIRouter(
    prefix="/empattendence",
    tags=["Employee Attendence"],
    # dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},)

# @router.get("/")
# async def view_empattendence():
#     pass
#     return 
# @router.get("/{empattendence_id}")
# async def search_empattendence():
#     pass
#     return 

# @router.post("/markattendance/{empattendenced_id}")
# async def mark_empattendence(empattendence_id : str):
#     pass
#     return 


# @router.get("/viewreport/{empattendenced_id}")
# async def view_empattendence_report(empattendence_id : str):
#     pass
#     return 


# @router.put("/modify/{empattendence_id}")
# async def modify_empattendence(empattendence_id: str):
#     pass

@router.get("/" )
async def view_Emp_Attendence2():
    response = await viewEmp_Attendence2()
    if response: 
        return {
            "status " : status.HTTP_200_OK, 
            "Emp_Attendence2 list" : response }
    return {"error": status.HTTP_204_NO_CONTENT} 


# @router.get("/{Emp_Attendence2_id}")
# async def search_Emp_Attendence2(Emp_Attendence2_id:str):
#     # print(Emp_Attendence2_id)
#     response = await searchEmp_Attendence2(Emp_Attendence2_id)
#     return response



@router.post("/")
async def mark_Emp_Attendence2(Emp_Attendence2 : employeeattendance2):
    response = await addEmp_Attendence2(Emp_Attendence2.dict())
    if response==True:
        return {"response ": "Successfully added . . .",
            "status" : status.HTTP_200_OK}       
    return {"response" : response, "status" :status.HTTP_203_NON_AUTHORITATIVE_INFORMATION }


@router.put("/modify/{Emp_Attendence2_id}")
async def modify_Emp_Attendence2(Emp_Attendence2_id: str , data : employeeattendance2_modify):
    response = await modifyEmp_Attendence2(Emp_Attendence2_id, data.dict(exclude_none=True))
    return response


@router.delete('/{id}')
async def delete_modify_id(id: str):
    
    response = await deleteEmp_Attendence2id(id)
    if not response:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'No record with id: {id} found')
    return { "Status":"Succesfully deleted ",
        "status_code " : status.HTTP_200_OK}

