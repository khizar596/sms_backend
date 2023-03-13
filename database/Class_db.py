from settings import sms_db
from fastapi import HTTPException
from bson import ObjectId
from models.Class import Class
col_Class = sms_db.Class



async def viewClass():
    Classs=[]
    cursor = col_Class.find({})

    for document in cursor:
        Classs.append((Class(**document)))
    return Classs

async def searchClass(Class_id : str)->dict:

    document=  col_Class.find_one({"_id": ObjectId(Class_id)},{'_id': 0}) 
    
    if not document:

        raise HTTPException(status_code=404, detail="document not found")
    
    return document


async def addClass(details):
    Classdetails= details
    
    col_Class.insert_one(Classdetails) # Changing ki hab 
    return True

async def modifyClass(Class_id:str , details):
    col_Class.update_one({"_id": ObjectId(Class_id)}, {"$set": details})
    return {"Succesfully updated the record"}

async def deleteclassid(Class_id:str):
    col_Class.delete_one({'_id': ObjectId(Class_id)})
    return True
