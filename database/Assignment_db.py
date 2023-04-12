from settings import sms_db
from fastapi import HTTPException
from bson import ObjectId
from models.Assignment import Assignment
from database.Chatbox_db import col_Classsubject
col_Assignment = sms_db.Assignment



async def viewAssignment():
    Assignments=[]
    cursor = col_Assignment.find({})

    for document in cursor:
        Class_subjectid_relation = col_Classsubject.find_one({"_id": ObjectId(document['Class_subjectid'])}, {'_id': 0})
        document['Class_subjectid']=Class_subjectid_relation

        document['_id']=str(document['_id'])
        Assignments.append(document)
    return Assignments

async def searchAssignment(Assignment_id : str)->dict:

    document=  col_Assignment.find_one({"_id": ObjectId(Assignment_id)},{'_id': 0}) 
    if not document:

        raise HTTPException(status_code=404, detail="document not found")
    Class_subjectid_relation = col_Classsubject.find_one({"_id": ObjectId(document['Class_subjectid'])}, {'_id': 0})
    document['Class_subjectid']=Class_subjectid_relation
    return document


async def addAssignment(details):
    Assignmentdetails= details
    Class_subjectid_relation = col_Classsubject.find_one({"_id": ObjectId(Assignmentdetails['Class_subjectid'])}, {'_id': 0})
    if not None and Class_subjectid_relation:
        col_Assignment.insert_one(Assignmentdetails) # Changing ki hab 
        return True
    
    raise HTTPException(status_code=403)


async def modifyAssignment(Assignment_id: str, details: dict):
    if details.get('Class_subjectid'):
        try:
            col_Classsubject.find_one({"_id": ObjectId(details['Class_subjectid'])}, {'_id': 0})
        except:
            return HTTPException(404)    
    else:
        pass
        
    col_Assignment.update_one({"_id": ObjectId(Assignment_id)}, {"$set": details})
    return {"Success": "Assignment record updated successfully"}


async def deleteAssignmentid(Assignment_id:str):
    col_Assignment.delete_one({'_id': ObjectId(Assignment_id)})
    return True
