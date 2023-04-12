from models.Fee import Fee
from settings import sms_db
from fastapi import HTTPException,status
from bson import ObjectId
from database.Student_db import col_student
col_fee = sms_db.fee




async def viewfee():
    fees=[] 
    cursor = col_fee.find({})

    for document in cursor:
        Student_id_check = str(document['Studentid'])
        student_found=  col_student.find_one({"_id": ObjectId(Student_id_check)},{'_id': 0})
        if student_found:
            document['Studentid']=student_found
            col_fee.insert_one(document) 
            return True
        fees.append(document)
    return fees

async def searchfee(fee_id : str)->dict:

    document=  col_fee.find_one({"_id": ObjectId(fee_id)},{'_id': 0}) 
       
    if not document:

        raise HTTPException(status_code=404, detail="Item not found")
    Student_id_check = str(document['Studentid'])
    student_found=  col_student.find_one({"_id": ObjectId(Student_id_check)},{'_id': 0})
    if student_found:
        # document['_id']=str(document['_id'])
        document['Studentid']=student_found
        return document
    raise  HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'No record with id: {Student_id_check} found')

async def addfee(details):
    feedetails= details
    Student_id_check = str(feedetails['Studentid'])
    student_found=  col_student.find_one({"_id": ObjectId(Student_id_check)},{'_id': 0})
    if student_found:
        # feedetails['Studentid']=student_found
        col_fee.insert_one(feedetails) 
        return True
    return {"Id error":"Id of student doesn't exist"}


async def modifyfee(fee_id:str , details):
    Student_id_check = str(details['Studentid'])
    if Student_id_check:
        student_found=  col_student.find_one({"_id": ObjectId(Student_id_check)},{'_id': 0})
        if student_found:
            pass
        else:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'No record with id: {Student_id_check} found')
        # details['Studentid']=student_found
    col_fee.update_one({"_id": ObjectId(fee_id)}, {"$set": details})
    return {"Succesfully updated the record"}



async def deletebyid(fee_id:str):
    col_fee.delete_one({'_id': ObjectId(fee_id)})
    return True
