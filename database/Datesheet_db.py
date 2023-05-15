from settings import sms_db
from fastapi import HTTPException
from models.Datesheet import Datesheet 
from bson import ObjectId
col_datesheet = sms_db.Datesheet
from database.Classsubject_db import col_Classsubject
from database.Section_db import col_Section
from database.Exam_db import col_Exam


async def viewdatesheet():
    datesheets=[]
   
    cursor = col_datesheet.find({})
   
    for document in cursor:
        classsubj_id_check = str(document['Class_subjectid'])
        Class_subjectid_found=  col_Classsubject.find_one({"_id": ObjectId(classsubj_id_check)},{'_id': 0})
        sectionid_check = str(document['Sectionid'])
        sectionid_found=  col_Section.find_one({"_id": ObjectId(sectionid_check)},{'_id': 0})
        Examid_check = str(document['Examid'])
        Examid_found=  col_Exam.find_one({"_id": ObjectId(Examid_check)},{'_id': 0})
        
        if Class_subjectid_found and Examid_found:
            document['_id']=str(document['_id'])
            document['Examid']=Examid_found
            document['Sectionid']=sectionid_found
            document['Class_subjectid']=Class_subjectid_found
            datesheets.append(document)
    return datesheets
    

async def searchdatesheet(datesheet_id : str)->dict:

    document=  col_datesheet.find_one({"_id": ObjectId(datesheet_id)},{'_id': 0}) 
    
    if not document:

        raise HTTPException(status_code=404, detail="document not found")
    classsubj_id_check = str(document['Class_subjectid'])
    Class_subjectid_found=  col_Classsubject.find_one({"_id": ObjectId(classsubj_id_check)},{'_id': 0})
    sectionid_check = str(document['Sectionid'])
    sectionid_found=  col_Section.find_one({"_id": ObjectId(sectionid_check)},{'_id': 0})
    Examid_check = str(document['Examid'])
    Examid_found=  col_Exam.find_one({"_id": ObjectId(Examid_check)},{'_id': 0})
        
    if Class_subjectid_found and Examid_found:
        document['Examid']=Examid_found
        document['Sectionid']=sectionid_found

        document['Class_subjectid']=Class_subjectid_found
        return document
    raise ValueError

async def adddatesheet(details):
    classsubj_id_check = str(details['Class_subjectid'])
    Class_subjectid_found=  col_Classsubject.find_one({"_id": ObjectId(classsubj_id_check)},{'_id': 0})
    Examid_check = str(details['Examid'])
    Examid_found=  col_Exam.find_one({"_id": ObjectId(Examid_check)},{'_id': 0})
    sectionid_check = str(details['Sectionid'])
    sectionid_found=  col_Section.find_one({"_id": ObjectId(sectionid_check)},{'_id': 0})

    if Class_subjectid_found!=None and Examid_found!=None and sectionid_found!=None:
        col_datesheet.insert_one(details) # Changing ki hab 
        return True
    raise HTTPException(status_code=403,detail="Details are not valid")

async def modifydatesheet(datesheet_id:str , details):
    if 'Sectionid' in details:
        try:
            
            col_Section.find_one({"_id": ObjectId( details['Sectionid'])},{'_id': 0})
        except:
            raise HTTPException(204, "Enter correct Examid")
    if 'Class_subjectid' in details:
        try:
            col_Classsubject.find_one({"_id": ObjectId( details['Class_subjectid'])},{'_id': 0})    
        except:
            raise HTTPException(204,"Enter correct Student id")
    if 'Examid' in details:
        try:
            
            col_Exam.find_one({"_id": ObjectId( details['Examid'])},{'_id': 0})
        except:
            raise HTTPException(204, "Enter correct Examid")
    
    col_datesheet.update_one({"_id": ObjectId(datesheet_id)}, {"$set": details})
    return {"Succesfully updated the record"}

async def deletedatesheetid(datesheet_id:str):
    col_datesheet.delete_one({'_id': ObjectId(datesheet_id)})
    return True
