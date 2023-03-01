from settings import sms_db
from fastapi import HTTPException
from models.Timetable import Timetable
from bson import ObjectId
from database.Section_db import col_Section
from database.Classsubject_db import col_Classsubject
from database.Teacher_db import col_Teacher
col_timetable = sms_db.Timetable



async def viewtimetable():
    col_timetables=[]
   
    cursor = col_timetable.find({})
   
    for document in cursor:
        col_timetables.append((Timetable(**document)))
    return col_timetables
    

async def searchtimetable(timetable_id : str)->dict:

    document=  col_timetable.find_one({"_id": ObjectId(timetable_id)},{'_id': 0}) 
    
    if not document:

        raise HTTPException(status_code=404, detail="document not found")
    
    return document


async def addtimetable(details):
    timetabledetails= details
    Teacher_relation=  [col_Teacher.find_one({"_id": ObjectId( timetabledetails['Teacherid'][0])},{'_id': 0})]
    timetabledetails['Teacherid'] = Teacher_relation

     # Check if there's already a timetable for this teacher at the same time
    conflict_query = {
    "Teacherid": timetabledetails['Teacherid'],
    "day": timetabledetails['day'],
    "$or": [
        {"start_time": {"$lt": timetabledetails['end_time']}, "end_time": {"$gt": timetabledetails['start_time']}},
        {"start_time": timetabledetails['start_time'], "end_time": timetabledetails['end_time']}
    ]
    }
    
    conflicting_timetable = col_timetable.find_one(conflict_query)
    if conflicting_timetable:
            raise HTTPException(status_code=409, detail="Teacher has a conflicting timetable")
    try:
        classSub_relation=  [col_Classsubject.find_one({"_id": ObjectId( timetabledetails['Class_subjectid'][0])},{'_id': 0})]
        Section_relation=  [col_Section.find_one({"_id": ObjectId( timetabledetails['Sectionid'][0])},{'_id': 0})]

        if classSub_relation!=None or Section_relation !=None :
            timetabledetails['Teacherid'] = Teacher_relation

            timetabledetails['Class_subjectid'] = classSub_relation
            timetabledetails['Sectionid'] = Section_relation
            col_timetable.insert_one(timetabledetails) # Changing ki hab 
            return True
    except :
            raise HTTPException(status_code=409, detail="Timetable entry already exists")

async def modifytimetable(timetable_id:str , details):
    timetabledetails= details
    Teacher_relation=  [col_Teacher.find_one({"_id": ObjectId( timetabledetails['Teacherid'][0])},{'_id': 0})]
    timetabledetails['Teacherid'] = Teacher_relation

     # Check if there's already a timetable for this teacher at the same time
    conflict_query = {
    "Teacherid": timetabledetails['Teacherid'],
    "day": timetabledetails['day'],
    "$or": [
        {"start_time": {"$lt": timetabledetails['end_time']}, "end_time": {"$gt": timetabledetails['start_time']}},
        {"start_time": timetabledetails['start_time'], "end_time": timetabledetails['end_time']}
    ]
    }
    
    conflicting_timetable = col_timetable.find_one(conflict_query)
    if conflicting_timetable:
            raise HTTPException(status_code=409, detail="Teacher has a conflicting timetable")
    try:
        classSub_relation=  [col_Classsubject.find_one({"_id": ObjectId( timetabledetails['Class_subjectid'][0])},{'_id': 0})]
        Section_relation=  [col_Section.find_one({"_id": ObjectId( timetabledetails['Sectionid'][0])},{'_id': 0})]

        if classSub_relation!=None: 
            timetabledetails['Class_subjectid'] = classSub_relation
        if Section_relation !=None :
            timetabledetails['Sectionid'] = Section_relation
        col_timetable.update_one({"_id": ObjectId(timetable_id)}, {"$set": timetabledetails})
        return {"Succesfully updated the record"}        
            
    except :
        raise HTTPException(status_code=409, detail="Timetable entry already exists")

    

async def deletetimetableid(timetable_id:str):
    col_timetable.delete_one({'_id': ObjectId(timetable_id)})
    return True
