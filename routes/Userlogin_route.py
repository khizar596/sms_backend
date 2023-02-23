from fastapi import APIRouter, HTTPException ,status
from models.Users_login import AuthDetails
from database.Student_db import col_student as cols
from database.Admin_db import col_Admin as cola
from database.Employee_db import col_employee as cole
from database.Parents_db import col_parent as colp
from database.auth import (
   AuthHandler
 
   
)
auth_handler= AuthHandler()
users= []

router = APIRouter(
    prefix="/login",
    tags=["Userlogin"],
    # dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}})

@router.post("/")
async def login(auth_details : AuthDetails):
    user = None
    for x in cola.find({}):
        
        try:
            if x['email'] == auth_details.email:
                user={}
                user['_id']=x['_id']
                user['email']=x['email']
                user['name']=x['name']
                user['password']=x['password']
                user['role']=x['role']  

                break
        except:
            pass  
    for b in cole.find({}):
        try:
            if b['email'] == auth_details.email:
                user={}
                user['_id']=b['_id']
                user['email']=b['email']
                user['cnic']=b['cnic']
                user['parent_name']=b['parent_name']
                user['role']=b['role']  
                user['password']=b['password']
                break
        except:
            pass  
    for c in colp.find({}):
        try:
            if c['email'] == auth_details.email:
                user={}
                user['_id']=c['_id']
                user['email']=c['email']
                user['cnic']=c['cnic']
                user['name']=c['name']
                user['role']=c['role']  
                user['password']=c['password']
                break
        except:
            pass  
    for d in cols.find({}):
        try:
            if d['email'] == auth_details.email:
                user={}
                user['_id']=d['_id']
                user['email']=d['email']
                user['cnic']=d['cnic']
                user['first_name']=d['first_name']
                user['last_name']=d['last_name']
                user['parent_name']=d['parent_name']
                user['role']=d['role']  
                user['password']=d['password']
                break
        except:
            pass  
  
    if (user is None) or (not auth_handler.verify_password(auth_details.password , user['password'])):
        raise HTTPException(status_code=401 , detail = "Invalid email and/or password")
    del user['password']

    token,details = auth_handler.encode_token(user)
    return { "token ": token ,
    "details": details
    }
  