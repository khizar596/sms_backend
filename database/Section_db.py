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
        Sections.append((Section(**document)))
    return Sections

async def searchSection(Section_id : str)->dict:

    document=  col_Section.find_one({"_id": ObjectId(Section_id)},{'_id': 0}) 
    if not document:
        raise HTTPException(status_code=404, detail="document not found")
    return document


async def addSection(details):
    Sectiondetails= details
     
    Classid_relation=  [col_Class.find_one({"_id": ObjectId( Sectiondetails['Classid'][0])},{'_id': 0})]
    if Classid_relation!=None :
        Sectiondetails['Classid'] = Classid_relation
        col_Section.insert_one(Sectiondetails) 
        return True

async def modifySection(Section_id:str , details):
    Sectiondetails= details    
    Classid_relation=  [col_Class.find_one({"_id": ObjectId( Sectiondetails['Classid'][0])},{'_id': 0})]
    if Classid_relation!=None:
        Sectiondetails['Classid'] = Classid_relation
        col_Section.update_one({"_id": ObjectId(Section_id)}, {"$set": details})
    return {"Succesfully updated the record"}
    
    
async def deleteSectionid(Section_id:str):
    col_Section.delete_one({'_id': ObjectId(Section_id)})
    return True
