from settings import sms_db
from fastapi import HTTPException
from bson import ObjectId
from database.auth import AuthHandler,colr
from models.Admin import Admin2
col_Admin = sms_db.Admin
auth_handler=AuthHandler()


async def viewAdmin():
    Admins=[]
    cursor = col_Admin.find({'role.0.name':'admin'})

    for document in cursor:
        Admins.append((Admin2(**document)))
    return Admins

# def addAdmin():
#     hashed = auth_handler.get_password_hash(password='admin123')

#     Admindetails=  {
#                                "name ": "Admin",
#                                "password":f"{hashed}"
#     }   
                                                            
#                 }
    
    # col_Admin.insert_one(Admindetails) # Changing ki hab 
    # return True

async def modifyAdmin(Admin_id:str , details):
    if not details['email'] or details['password']:
        return {"Please both the credentials email and password"}
    hashed = auth_handler.get_password_hash(details['password'])
    details['password']=hashed
    if details['role']:
        roles_relation=details['role']
        role_relation= [colr.find_one({"_id": ObjectId(roles_relation[0]),'role.0.name':'admin'},{'_id': 0})]
        details['role']=role_relation
        
    col_Admin.update_one({"_id": ObjectId(Admin_id)}, {"$set": details})
    return {"Succesfully updated the record"}
