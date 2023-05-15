from models.Parent import Parent , Parent_modify
from settings import sms_db
from fastapi import HTTPException
from bson import ObjectId
from database.auth import AuthHandler,colr
auth_handler=AuthHandler()
col_parent = sms_db.parent




async def viewparent():
    parents=[]
    cursor = col_parent.find({})
    for document in cursor:
        # document['parentid']=list(document['parentid'])
        document['_id']=str(document['_id'])
        parents.append(document)

        # parents.append((Student(**document)))
        # print(parents)
    return parents

async def searchparent(parent_id : str)->dict:

    document=  col_parent.find_one({"_id": ObjectId(parent_id)},{'_id': 0}) 
    # document=  col_parent.find_one({"_id": ObjectId(parent_id)}) #ROLA WALA JAGA
    
    if not document:

        raise HTTPException(status_code=404, detail="Item not found")
    
    return document


async def addparent(details):
    parentdetails= details
    
    roles_relation=parentdetails['role']
    try:
        role_relation= [colr.find_one({"_id": ObjectId(roles_relation[0])},{'_id': 0})]
    except:
        raise HTTPException(204,"Roles not found")
    if details['password']:
        hashed = auth_handler.get_password_hash(details['password'])
        details['password']=hashed
    cursor = col_parent.find({})
    if role_relation:
            parentdetails['role']=role_relation
    for document in cursor:
        if document['cnic']==parentdetails['cnic']:
            response= {"CNIC " : "already exist "}
            return response
        elif document['email']==parentdetails['email']:
            response={"Email " : "already exist "}    
            return response
    if role_relation[0]['name']=="Parent" and details['password']!=None:
        col_parent.insert_one(parentdetails) # Changing ki hab 
        return True
    return "Fill the form carefully "

async def modifyparent(parent_id:str , details):
    try:
        if details['password']!=None:
            hashed = auth_handler.get_password_hash(details['password'])
            details['password']=hashed
        
        roles_relation=details['role']
        role_relation= [colr.find_one({"_id": ObjectId(roles_relation[0])},{'_id': 0})]

        if role_relation!=None:
            details['role']=role_relation
    except:
        pass
    col_parent.update_one({"_id": ObjectId(parent_id)}, {"$set": details})
    return {"Succesfully updated the record"}

async def deletebyid(parent_id:str):
    col_parent.delete_one({'_id': ObjectId(parent_id)})
    return True
