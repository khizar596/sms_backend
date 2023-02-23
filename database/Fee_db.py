from models.Fee import Fee
from settings import sms_db
from fastapi import HTTPException
from bson import ObjectId
from database.Student_db import col_student
col_fee = sms_db.fee




async def viewfee():
    fees=[] 
    cursor = col_fee.find({})

    for document in cursor:
        fees.append((Fee(**document)))
    return fees

async def searchfee(fee_id : str)->dict:

    document=  col_fee.find_one({"_id": ObjectId(fee_id)},{'_id': 0})    
    if not document:

        raise HTTPException(status_code=404, detail="Item not found")
    
    return document


async def addfee(details):
    feedetails= details
    Student_id_check = feedetails['Studentid'][0]
    student_found=  [col_student.find_one({"_id": ObjectId(Student_id_check)},{'_id': 0})]
    if student_found:
        feedetails['Studentid']=student_found
        col_fee.insert_one(feedetails) 
        return True
    return {"Id error":"Id of student doesn't exist"}


async def modifyfee(fee_id:str , details):

    Student_id_check = details['Studentid'][0]
    student_found=  [col_student.find_one({"_id": ObjectId(Student_id_check)},{'_id': 0})]
    if student_found:
        details['Studentid']=student_found
        col_fee.update_one({"_id": ObjectId(fee_id)}, {"$set": details})
        return {"Succesfully updated the record"}



async def deletebyid(fee_id:str):
    col_fee.delete_one({'_id': ObjectId(fee_id)})
    return True
