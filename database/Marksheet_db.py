from models.Marksheet import Marksheet
from settings import sms_db
from fastapi import HTTPException
from bson import ObjectId
from database.Exam_db import col_Exam
from database.Student_db import col_student
col_marksheet = sms_db.Marksheets
from database.auth import AuthHandler

auth_handler=AuthHandler()


async def viewmarksheet():
    col_marksheets=[]
   
    cursor = col_marksheet.find({})
   
    for document in cursor:
        exam_relation=  col_Exam.find_one({"_id": ObjectId( document['Examid'])},{'_id': 0})
        student_relation=  col_student.find_one({"_id": ObjectId( document['Studentid'])},{'_id': 0,'first_name':1})    
        
        if exam_relation!=None and student_relation !=None :
            document['Examid'] = exam_relation
            document['Studentid'] = student_relation
            document['_id']=str(document['_id'])
            col_marksheets.append(document)
    return col_marksheets
    

async def searchmarksheet(marksheet_id : str)->dict:

    document=  col_marksheet.find_one({"_id": ObjectId(marksheet_id)},{'_id': 0}) 
    if not document:

        raise HTTPException(status_code=404, detail="document not found")
    try:
        exam_relation=  col_Exam.find_one({"_id": ObjectId( document['Examid'])},{'_id': 0})
        student_relation=  col_student.find_one({"_id": ObjectId( document['Studentid'])},{'_id': 0})    
    except:
        raise HTTPException(204, "Id relations not found")
    if exam_relation!=None and student_relation !=None :
        
        document['Examid'] = exam_relation
        document['Studentid'] = student_relation
        document['_id']=str(document['_id'])
    return document





async def addmarksheet(details):

    if 'Examid' in details:
        try:
            
            exam_relation=  col_Exam.find_one({"_id": ObjectId( details['Examid'])},{'_id': 0})
        except:
            raise HTTPException(204, "Enter correct Examid")
    if 'Studentid' in details:
        try:
            student_relation=  col_student.find_one({"_id": ObjectId( details['Studentid'])},{'_id': 0})    
        except:
            raise HTTPException(204,"Enter correct Student id")

    col_marksheet.insert_one(details) # Changing ki hab 
    return True

async def modifymarksheet(marksheet_id:str , details):
    if 'Examid' in details:
        try:
            exam_relation=  col_Exam.find_one({"_id": ObjectId( details['Examid'])},{'_id': 0})
        except:
            del details['Examid']
            
    if 'Studentid' in details:
        try:
            student_relation=  col_student.find_one({"_id": ObjectId( details['Studentid'])},{'_id': 0})    
        except:
            del details['Studentid']
            
    col_marksheet.update_one({"_id": ObjectId(marksheet_id)}, {"$set": details})
    return {"Succesfully updated the record"}




async def deletemarksheetid(marksheet_id:str):
    col_marksheet.delete_one({'_id': ObjectId(marksheet_id)})
    return True
