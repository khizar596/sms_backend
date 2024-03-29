from settings import sms_db
from fastapi import HTTPException
from bson import ObjectId
from models.Class_subject import Class_subject
from database.Class_db import col_Class
from database.Courses_db import col_Course
from database.Employee_db import col_employee as cole
col_Classsubject = sms_db.Classsubject



async def viewClasssubject():
    Classsubjects=[]
    cursor = col_Classsubject.find({})
    
    for document in cursor:
        document['_id']=str(document['_id'])
        class_relation=  col_Class.find_one({"_id": ObjectId( document['Classid'])},{'_id': 0})
        Teacher_relation=  cole.find_one({"_id": ObjectId( document['Teacherid'])},{'_id': 0,'first_name':1})
        Course_relation=  col_Course.find_one({"_id": ObjectId( document['Courseid'])},{'_id': 0}) #ROLA WALA JAGA    
        if class_relation!=None or Course_relation !=None or Teacher_relation !=None :
            document['Classid'] = class_relation
            document['Courseid'] = Course_relation
            document['Teacherid'] = Teacher_relation            
            Classsubjects.append(document)
    return Classsubjects

async def searchClasssubject(Classsubject_id : str)->dict:

    document=  col_Classsubject.find_one({"_id": ObjectId(Classsubject_id)},{'_id': 0}) 
    
    if not document:

        raise HTTPException(status_code=404, detail="document not found")
    class_relation=  col_Class.find_one({"_id": ObjectId( document['Classid'])},{'_id': 0})
    Teacher_relation=  cole.find_one({"_id": ObjectId( document['Teacherid'])},{'_id': 0,'first_name':1})
    Course_relation=  col_Course.find_one({"_id": ObjectId( document['Courseid'])},{'_id': 0}) #ROLA WALA JAGA    
    if class_relation!=None or Course_relation !=None or Teacher_relation !=None :
        document['Classid'] = class_relation
        document['Courseid'] = Course_relation
        document['Teacherid'] = Teacher_relation 
    return document


async def addClasssubject(details):
    try:
        class_relation=  col_Class.find_one({"_id": ObjectId( details['Classid'])},{'_id': 0})
    except:
        raise HTTPException(204,"Class id not found")
    try:
        Teacher_relation=  cole.find_one({"_id": ObjectId(details['Teacherid']),'role.0.name':'Teacher'},{'_id': 0,'first_name':1})
    except:
        raise HTTPException(204,"Teacher not found")
    try:
        Course_relation=  col_Course.find_one({"_id": ObjectId( details['Courseid'])},{'_id': 0}) #ROLA WALA JAGA    
    except:
        raise HTTPException(204, "Course id not found")
    if class_relation!=None and Course_relation !=None and Teacher_relation !=None :
        col_Classsubject.insert_one(details) # Changing ki hab 
        return True

    return HTTPException(203, "Data is missing in database")

async def modifyClasssubject(Classsubject_id:str , details):
    if  "Classid" in details:
        class_relation=  col_Class.find_one({"_id": ObjectId( details['Classid'])},{'_id': 0})  

        if class_relation==None:
            del details['Classid']
    if "Teacherid" in details:
        Teacher_relation=  cole.find_one({"_id": ObjectId( details['Teacherid'])},{'_id': 0,'first_name':1})
        if Teacher_relation==None:
            del details['Teacherid']
    if "Courseid" in details:
        Course_relation=  col_Course.find_one({"_id": ObjectId( details['Courseid'])},{'_id': 0}) #ROLA WALA JAGA    
        
        if Course_relation==None:
            del details['Courseid']
        
    col_Classsubject.update_one({"_id": ObjectId(Classsubject_id)}, {"$set": details})
    return {"status":200,"Message":"Succesfully updated the record"}
async def deleteclasssubjectid(Classsubject_id:str):
    col_Classsubject.delete_one({'_id': ObjectId(Classsubject_id)})
    return True
