from fastapi import APIRouter, HTTPException ,status
from models.Users_login import AuthDetails
from database.Student_db import col_student as cols
from database.Admin_db import col_Admin as cola
from database.Employee_db import col_employee as cole
from database.Parents_db import col_parent as colp
from database.Teacher_db import col_Teacher as colT
from database.Staff2_db import col_Staff2 as colS
from database.HR2_db import col_HR2 as colhr
from database.Accountant2_db import col_Accountant2 as colA2
from database.StudentAdmin_db import col_StudentAdmin as colSA
from database.auth import (
   AuthHandler
 
   
)
auth_handler= AuthHandler()
users= []

router = APIRouter(
    prefix="/login",
    tags=["User login"],
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
                user['first_name']=b['first_name']
                user['last_name']=b['last_name']
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
    for T in colT.find({}):
        try:
            if T['email'] == auth_details.email:
                user={}

                user['_id']=T['_id']
                user['email']=T['email']
                user['first_name']=T['first_name']
                user['last_name']=T['last_name']
                user['password']=T['password']
                user['role']=T['role']  
                

                break
        except:
            pass
    for S in colS.find({}):
        try:
            if S['email'] == auth_details.email:
                user={}

                user['_id']=S['_id']
                user['email']=S['email']
                user['first_name']=S['first_name']
                user['last_name']=S['last_name']
                user['password']=S['password']
                user['role']=S['role']  
                

                break
        except:
            pass    
    for SA in colSA.find({}):
        try:
            if SA['email'] == auth_details.email:
                user={}

                user['_id']=SA['_id']
                user['email']=SA['email']
                user['first_name']=SA['first_name']
                user['last_name']=SA['last_name']
                user['password']=SA['password']
                user['role']=SA['role']  
                

                break
        except:
            pass  
    for A2 in colA2.find({}):
        try:
            if A2['email'] == auth_details.email:
                user={}

                user['_id']=A2['_id']
                user['email']=A2['email']
                user['first_name']=A2['first_name']
                user['last_name']=A2['last_name']
                user['password']=A2['password']
                user['role']=A2['role']  
                

                break
        except:
            pass  
    for HR in colhr.find({}):
        try:
            if HR['email'] == auth_details.email:
                user={}

                user['_id']=HR['_id']
                user['email']=HR['email']
                user['first_name']=HR['first_name']
                user['last_name']=HR['last_name']
                user['password']=HR['password']
                user['role']=HR['role']  
                

                break
        except:
            pass  
    if (user is None) or (not auth_handler.verify_password(auth_details.password , user['password'])):
        
        raise HTTPException(status_code=401 , detail = "Invalid email and/or password")
    else: 
        del user['password']

        token,details = auth_handler.encode_token(user)
        return { "token ": token ,
                 "details": details
        }