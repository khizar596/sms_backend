from settings import sms_db
from fastapi import HTTPException
from bson import ObjectId
from models.Section import Section
col_Section = sms_db.Section



async def viewSection():
    Sections=[]
    cursor = col_Section.find({})

    for document in cursor:
        Sections.append((Section(**document)))
    return Sections

# async def searchSection(Section_id : str)->dict:

#     document=  col_Section.find_one({"_id": ObjectId(Section_id)},{'_id': 0}) 
    
#     if not document:

#         raise HTTPException(status_code=404, detail="document not found")
    
#     return document


async def addSection(details):
    Sectiondetails= details
    
    col_Section.insert_one(Sectiondetails) 
    return True

async def modifySection(Section_id:str , details):
    col_Section.update_one({"_id": ObjectId(Section_id)}, {"$set": details})
    return {"Succesfully updated the record"}

async def deleteSectionid(Section_id:str):
    col_Section.delete_one({'_id': ObjectId(Section_id)})
    return True
