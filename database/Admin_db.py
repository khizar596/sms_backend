from settings import sms_db
from fastapi import HTTPException
from bson import ObjectId
from database.auth import AuthHandler
from models.Admin import Admin2
col_Admin = sms_db.Admin
auth_handler=AuthHandler()


async def viewAdmin():
    Admins=[]
    cursor = col_Admin.find({})

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
    hashed = auth_handler.get_password_hash(details['password'])
    details['password']=hashed
    col_Admin.update_one({"_id": ObjectId(Admin_id)}, {"$set": details})
    return {"Succesfully updated the record"}
