from fastapi import APIRouter, HTTPException, status
from models.Admin import Admin2
from database.Admin_db import modifyAdmin

router = APIRouter(
    prefix="/Admin",
    tags=["Admin"],
    # dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},)



@router.put("/edit/{admin_id}")
async def edit_admin(admin_id: str,  data :Admin2 ):
    response = await modifyAdmin(admin_id, data.dict(exclude_none=True))
    print(response)
    return { "Response":response,
        "status_code " : status.HTTP_200_OK}






