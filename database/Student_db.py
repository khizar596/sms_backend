from models.Student import Student
from settings import sms_db
from fastapi import HTTPException
from bson import ObjectId
col_student = sms_db.Student
from database.auth import AuthHandler
from models.Parent import Parent
from database.Class_db import col_Class
from database.Parents_db import col_parent
auth_handler=AuthHandler()


async def viewStudent():
    
    ParentDetails = [Parent(**parent) for parent in col_parent.find({})]    
    
    students=[]
    cursor = col_student.find({})
    for document in cursor:
        document['parentid']=ParentDetails
        students.append((Student(**document)))
        # print(students)
    return students

async def searchStudent(student_id : str)->dict:
    

    document=  col_student.find_one({"_id": ObjectId(student_id)},{'_id': 0}) #ROLA WALA JAGA    
    # document=  col_student.find_one({"_id": ObjectId(student_id)}) #ROLA WALA JAGA
    
    if not document:

        raise HTTPException(status_code=404, detail="Item not found")
    
    return document


async def enrollstudent(details):
    
    studentdetails= details
    cursor = col_student.find({})

    for document in cursor:
        if document['cnic']==studentdetails['cnic']:
            response= {"CNIC " : "already exist "}
            return response
        if document['email']==studentdetails['email']:
            response={"Email " : "already exist "}    
            return response
    
    #### PASWORD HASHED

    hashed = auth_handler.get_password_hash(studentdetails['password'])
    studentdetails['password']=hashed
    
    #### Relations 
    
    classsubject_relation=  [col_Class.find_one({"_id": ObjectId( studentdetails['class_subjectid'][0])},{'_id': 0})]
    parent_relation=  [col_parent.find_one({"_id": ObjectId( studentdetails['parentid'][0])},{'_id': 0})] #ROLA WALA JAGA    
    if parent_relation!=None or classsubject_relation !=None :
        studentdetails['parentid'] = (parent_relation)
        studentdetails['class_subjectid'] = classsubject_relation
        col_student.insert_one(studentdetails) # Changing ki hab 
        return True

async def modifystudent(student_id:str , details):
    studentdetails=details
    if details['password']:
        hashed = auth_handler.get_password_hash(details['password'])
        details['password']=hashed
    else: 
        return{'Enter password please '}


      #### MODIFY Relations 

    classsubject_relation=  [col_Class.find_one({"_id": ObjectId( studentdetails['class_subjectid'][0])},{'_id': 0})]
    parent_relation=  [col_parent.find_one({"_id": ObjectId( studentdetails['parentid'][0])},{'_id': 0})] #ROLA WALA JAGA    
    if parent_relation!=None and classsubject_relation !=None :
        studentdetails['parentid'] = (parent_relation)
        studentdetails['class_subjectid'] = classsubject_relation


        col_student.update_one({"_id": ObjectId(student_id)}, {"$set": details})
    return {"Succesfully updated the record"}

async def deletebyid(student_id:str):
    col_student.delete_one({'_id': ObjectId(student_id)})
    return True
