from models.Parent import Parent , Parent_modify
from settings import sms_db
from fastapi import HTTPException
from bson import ObjectId
from database.auth import AuthHandler
auth_handler=AuthHandler()
col_parent = sms_db.parent




async def viewparent():
    parents=[]
    cursor = col_parent.find({})

    for document in cursor:
        parents.append((Parent(**document)))
    return parents

async def searchparent(parent_id : str)->dict:

    document=  col_parent.find_one({"_id": ObjectId(parent_id)},{'_id': 0}) 
    # document=  col_parent.find_one({"_id": ObjectId(parent_id)}) #ROLA WALA JAGA
    
    if not document:

        raise HTTPException(status_code=404, detail="Item not found")
    
    return document


async def addparent(details):
    parentdetails= details
    if details['password']:
        hashed = auth_handler.get_password_hash(details['password'])
        details['password']=hashed
    # cursor = col_parent.find({})

    # for document in cursor:
    #     if document['cnic']==parentdetails['cnic']:
    #         response= {"CNIC " : "already exist "}
    #         return response
    #     elif document['email']==parentdetails['email']:
    #         response={"Email " : "already exist "}    
    #         return response
    col_parent.insert_one(parentdetails) # Changing ki hab 
    return True

async def modifyparent(parent_id:str , details):
    if details['password']:
        hashed = auth_handler.get_password_hash(details['password'])
        details['password']=hashed
    col_parent.update_one({"_id": ObjectId(parent_id)}, {"$set": details})
    return {"Succesfully updated the record"}

async def deletebyid(parent_id:str):
    col_parent.delete_one({'_id': ObjectId(parent_id)})
    return True
