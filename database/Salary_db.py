from settings import sms_db
from fastapi import HTTPException
from models.Salary2 import Salary2
from bson import ObjectId
col_Salary = sms_db.Salary



async def viewSalary():
    col_Salarys=[]
   
    cursor = col_Salary.find({})
   
    for document in cursor:
        col_Salarys.append((Salary2(**document)))
    return col_Salarys
    

async def searchSalary(Salary_id : str)->dict:

    document=  col_Salary.find_one({"_id": ObjectId(Salary_id)},{'_id': 0}) 
    
    if not document:

        raise HTTPException(status_code=404, detail="document not found")
    
    return document


async def addSalary(details):
    Salarydetails= details
    # feedetails= details
    # Student_id_check = feedetails['Studentid']
    # document=  col_student.find_one({"_id": ObjectId(Student_id_check)},{'_id': 0})    
    # if document:
    #     col_fee.insert_one(feedetails) # Changing ki hab 
    #     return True
    # return {"Id error":"Id of student doesn't exist"}

    col_Salary.insert_one(Salarydetails) # Changing ki hab 
    return True

async def modifySalary(Salary_id:str , details):
    col_Salary.update_one({"_id": ObjectId(Salary_id)}, {"$set": details})
    return {"Succesfully updated the record"}

async def deleteSalaryid(Salary_id:str):
    col_Salary.delete_one({'_id': ObjectId(Salary_id)})
    return True
