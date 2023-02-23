from models.Marksheet import Marksheet
from settings import sms_db
from fastapi import HTTPException
from bson import ObjectId
col_marksheet = sms_db.Marksheets



async def viewmarksheet():
    col_marksheets=[]
   
    cursor = col_marksheet.find({})
   
    for document in cursor:
        col_marksheets.append((Marksheet(**document)))
    return col_marksheets
    

async def searchmarksheet(marksheet_id : str)->dict:

    document=  col_marksheet.find_one({"_id": ObjectId(marksheet_id)},{'_id': 0}) 
    
    if not document:

        raise HTTPException(status_code=404, detail="document not found")
    
    return document


async def addmarksheet(details):
    marksheetdetails= details
    # feedetails= details
    # Student_id_check = feedetails['Studentid']
    # document=  col_student.find_one({"_id": ObjectId(Student_id_check)},{'_id': 0})    
    # if document:
    #     col_fee.insert_one(feedetails) # Changing ki hab 
    #     return True
    # return {"Id error":"Id of student doesn't exist"}

    col_marksheet.insert_one(marksheetdetails) # Changing ki hab 
    return True

async def modifymarksheet(marksheet_id:str , details):
    col_marksheet.update_one({"_id": ObjectId(marksheet_id)}, {"$set": details})
    return {"Succesfully updated the record"}

async def deletemarksheetid(marksheet_id:str):
    col_marksheet.delete_one({'_id': ObjectId(marksheet_id)})
    return True
