from fastapi import APIRouter, HTTPException, status,Depends
from models.Admin import Admin2
from database.Admin_db import modifyAdmin
from database.auth import AuthHandler
auth_handler=AuthHandler()
router = APIRouter(
    prefix="/Admin",
    tags=["Admin"],
    dependencies=[Depends(auth_handler.auth_wrapper)],
    responses={404: {"description": "Not found"}}
    )



@router.put("/edit/{admin_id}")
async def edit_admin(admin_id: str,  data :Admin2 ,user = Depends(auth_handler.auth_wrapper)):
    auth_handler.has_permission(user, 'edit_admin')

    response = await modifyAdmin(admin_id, data.dict(exclude_none=True))
    return { "Response":response,
        "status_code " : status.HTTP_200_OK}






