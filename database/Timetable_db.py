from settings import sms_db
from fastapi import HTTPException
from models.Timetable import Timetable
from bson import ObjectId
from database.Section_db import col_Section
from database.Classsubject_db import col_Classsubject
from database.Teacher_db import col_employee as cole
col_timetable = sms_db.Timetable



async def viewtimetable():
    col_timetables=[]
   
    cursor = col_timetable.find({})
   
    for document in cursor:
        classSub_relation=  col_Classsubject.find_one({"_id": ObjectId( document['Class_subjectid'])},{'_id': 0})
        Section_relation=  col_Section.find_one({"_id": ObjectId( document['Sectionid'])},{'_id': 0})

        Teacher_relation=  cole.find_one({"_id": ObjectId( document['Teacherid'])},{'_id': 0,'first_name':1})
        document['Class_subjectid'] = classSub_relation
        document['Sectionid'] = Section_relation

        document['Teacherid'] = Teacher_relation
        document['_id']= str(document['_id'])
        col_timetables.append(document)
    return col_timetables
    

async def searchtimetable(timetable_id : str)->dict:

    document=  col_timetable.find_one({"_id": ObjectId(timetable_id)},{'_id': 0}) 
    
    if not document:

        raise HTTPException(status_code=404, detail="document not found")
    classSub_relation=  col_Classsubject.find_one({"_id": ObjectId( document['Class_subjectid'])},{'_id': 0})
    Section_relation=  col_Section.find_one({"_id": ObjectId( document['Sectionid'])},{'_id': 0})

    Teacher_relation=  cole.find_one({"_id": ObjectId( document['Teacherid'])},{'_id': 0,'first_name':1})
    document['Class_subjectid'] = classSub_relation
    document['Sectionid'] = Section_relation

    document['Teacherid'] = Teacher_relation
    return document


async def addtimetable(details):
    try:
        Teacher_relation=  cole.find_one({"_id": ObjectId( details['Teacherid'])},{'_id': 0})
         # Check if there's already a timetable for this teacher at the same time
        if Teacher_relation==None:
            raise HTTPException(204,"Details of Teacher id not found")
        conflict_query = {
        "Teacherid": details['Teacherid'],
        "day": details['day'],
        "$or": [
            {"start_time": {"$lt": details['end_time']}, "end_time": {"$gt": details['start_time']}},
            {"start_time": details['start_time'], "end_time": details['end_time']}
        ]
        }
        conflicting_timetable = col_timetable.find_one(conflict_query)
        if conflicting_timetable:
                raise HTTPException(status_code=409, detail="Teacher has a conflicting timetable")

    except:
        raise HTTPException(204,"Teacher detils not found")


    try:
        classSub_relation=  col_Classsubject.find_one({"_id": ObjectId( details['Class_subjectid'])},{'_id': 0})
    except:
        raise HTTPException(204,"class subject details not found")
    try:
        Section_relation=  col_Section.find_one({"_id": ObjectId( details['Sectionid'])},{'_id': 0})
    except:
        raise HTTPException(204,"class subject details not found")
    if classSub_relation!=None and Section_relation !=None and Teacher_relation!=None :
        col_timetable.insert_one(details) # Changing ki hab 
        return True
    raise HTTPException(status_code=409, detail="Check details")

async def modifytimetable(timetable_id:str , details):
    if "Teacherid" in details:
        try:
            Teacher_relation=  cole.find_one({"_id": ObjectId( details['Teacherid'])},{'_id': 0})
            conflict_query = {
            "Teacherid": details['Teacherid'],
            "day": details['day'],
            "$or": [
                {"start_time": {"$lt": details['end_time']}, "end_time": {"$gt": details['start_time']}},
                {"start_time": details['start_time'], "end_time": details['end_time']}]}
            conflicting_timetable = col_timetable.find_one(conflict_query)
            if conflicting_timetable:
                raise HTTPException(status_code=409, detail="Teacher has a conflicting timetable")
        except:
            raise HTTPException(204, "Deatils of teacherid not found")


    if "Class_subjectid" in details:
        try:
            classSub_relation=  col_Classsubject.find_one({"_id": ObjectId( details['Class_subjectid'])},{'_id': 0})
            if classSub_relation!=None:
                pass
            else:
                raise HTTPException(204,"deatils of subject not found")        
        except:
            raise HTTPException(204,"deatils of subject not found")        
    if "Sectionid" in details:
        try:
            Section_relation=  col_Section.find_one({"_id": ObjectId( details['Sectionid'])},{'_id': 0})
            if Section_relation !=None :
                pass
            else:
                raise HTTPException(204,"deatils of subject not found")   
        except:
            raise HTTPException(204,"deatils of subject not found")   

    col_timetable.update_one({"_id": ObjectId(timetable_id)}, {"$set": details})
    return {"Succesfully updated the record"}        


    

async def deletetimetableid(timetable_id:str):
    col_timetable.delete_one({'_id': ObjectId(timetable_id)})
    return True
