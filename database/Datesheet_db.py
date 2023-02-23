from settings import sms_db
from fastapi import HTTPException
from models.Datesheet import Datesheet 
from bson import ObjectId
col_datesheet = sms_db.Datesheet



async def viewdatesheet():
    col_datesheets=[]
   
    cursor = col_datesheet.find({})
   
    for document in cursor:
        col_datesheets.append((Datesheet(**document)))
    return col_datesheets
    

async def searchdatesheet(datesheet_id : str)->dict:

    document=  col_datesheet.find_one({"_id": ObjectId(datesheet_id)},{'_id': 0}) 
    
    if not document:

        raise HTTPException(status_code=404, detail="document not found")
    
    return document


async def adddatesheet(details):
    datesheetdetails= details
    # feedetails= details
    # Student_id_check = feedetails['Studentid']
    # document=  col_student.find_one({"_id": ObjectId(Student_id_check)},{'_id': 0})    
    # if document:
    #     col_fee.insert_one(feedetails) # Changing ki hab 
    #     return True
    # return {"Id error":"Id of student doesn't exist"}

    col_datesheet.insert_one(datesheetdetails) # Changing ki hab 
    return True

async def modifydatesheet(datesheet_id:str , details):
    col_datesheet.update_one({"_id": ObjectId(datesheet_id)}, {"$set": details})
    return {"Succesfully updated the record"}

async def deletedatesheetid(datesheet_id:str):
    col_datesheet.delete_one({'_id': ObjectId(datesheet_id)})
    return True
