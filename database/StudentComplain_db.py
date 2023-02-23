from settings import sms_db
from fastapi import HTTPException
from bson import ObjectId
col_Std_comp = sms_db.Std_complain
from models.StudentComplain import StudentComplain



async def viewStd_comp():
    Std_comps=[]
    cursor = col_Std_comp.find({})

    for document in cursor:
        Std_comps.append((StudentComplain(**document)))
    return Std_comps

async def searchStd_comp(Std_comp_id : str)->dict:

    document=  col_Std_comp.find_one({"_id": ObjectId(Std_comp_id)},{'_id': 0}) 
    
    if not document:

        raise HTTPException(status_code=404, detail="Item not found")
    
    return document


async def addStd_comp(details):
    Std_compdetails= details
    
    col_Std_comp.insert_one(Std_compdetails) # Changing ki hab 
    return True

async def modifyStd_comp(Std_comp_id:str , details):
    col_Std_comp.update_one({"_id": ObjectId(Std_comp_id)}, {"$set": details})
    return {"Succesfully updated the record"}

async def deletebyid(Std_comp_id:str):
    col_Std_comp.delete_one({'_id': ObjectId(Std_comp_id)})
    return True
