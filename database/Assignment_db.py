from settings import sms_db
from fastapi import HTTPException
from bson import ObjectId
from models.Assignment import Assignment
col_Assignment = sms_db.Assignment



async def viewAssignment():
    Assignments=[]
    cursor = col_Assignment.find({})

    for document in cursor:
        Assignments.append((Assignment(**document)))
    return Assignments

async def searchAssignment(Assignment_id : str)->dict:

    document=  col_Assignment.find_one({"_id": ObjectId(Assignment_id)},{'_id': 0}) 
    
    if not document:

        raise HTTPException(status_code=404, detail="document not found")
    
    return document


async def addAssignment(details):
    Assignmentdetails= details
    
    col_Assignment.insert_one(Assignmentdetails) # Changing ki hab 
    return True

async def modifyAssignment(Assignment_id:str , details):
    col_Assignment.update_one({"_id": ObjectId(Assignment_id)}, {"$set": details})
    return {"Succesfully updated the record"}

async def deleteAssignmentid(Assignment_id:str):
    col_Assignment.delete_one({'_id': ObjectId(Assignment_id)})
    return True
