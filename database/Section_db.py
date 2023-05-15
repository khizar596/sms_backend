from settings import sms_db
from fastapi import HTTPException
from bson import ObjectId
from models.Section import Section
from database.Class_db import col_Class
col_Section = sms_db.Section



async def viewSection():
    
    Sections=[]
    
    cursor = col_Section.find({})

    for document in cursor:
        Classid_relation=  col_Class.find_one({"_id": ObjectId( document['Classid'])},{'_id': 0})
        document['Classid'] = Classid_relation
        document['_id']= str(document['_id'])
        Sections.append(document)
    return Sections

async def searchSection(Section_id : str)->dict:

    document=  col_Section.find_one({"_id": ObjectId(Section_id)},{'_id': 0}) 
    if not document:
        raise HTTPException(status_code=404, detail="document not found")
    try:
        Classid_relation=  col_Class.find_one({"_id": ObjectId( document['Classid'])},{'_id': 0})
        document['Classid'] = Classid_relation
    except:
        raise HTTPException(204,"Class id missing")
    return document


async def addSection(details):
    try:
        Classid_relation=  col_Class.find_one({"_id": ObjectId( details['Classid'])},{'_id': 0})
    except:
        raise HTTPException(204,"Details missing of Class id")
    if Classid_relation!=None :
        col_Section.insert_one(details) 
        return True

async def modifySection(Section_id:str , details):
    if "Classid" in details:
        try:
            Classid_relation=  col_Class.find_one({"_id": ObjectId( details['Classid'])},{'_id': 0})
        except:
            raise HTTPException(204,"Class id is not correct")
        if Classid_relation!=None:
            pass
        else:
            raise HTTPException(204,"Class id not exist")
    col_Section.update_one({"_id": ObjectId(Section_id)}, {"$set": details})
    return {"Succesfully updated the record"}
    
    
async def deleteSectionid(Section_id:str):
    col_Section.delete_one({'_id': ObjectId(Section_id)})
    return True
