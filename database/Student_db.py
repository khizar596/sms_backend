from models.Student import Student
from settings import sms_db
from fastapi import HTTPException
from bson import ObjectId
col_student = sms_db.Student
from database.auth import AuthHandler,colr
from models.Parent import Parent
from database.Class_db import col_Class
from database.Parents_db import col_parent
auth_handler=AuthHandler()


async def viewStudent():
    
    # ParentDetails = [Parent(**parent) for parent in col_parent.find({})]    
    
    students=[]
    cursor = col_student.find({'role.0.name':'student'})
    for document in cursor:
        # document['parentid']=list(document['parentid'])
        students.append((Student(**document)))
        # print(students)
    return students

async def searchStudent(student_id : str)->dict:
    

    document=  col_student.find_one({"_id": ObjectId(student_id),'role.0.name':'student'},{'_id': 0}) #ROLA WALA JAGA    
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
    
    class_relation=  [col_Class.find_one({"_id": ObjectId( studentdetails['class_id'][0])},{'_id': 0})]
    parent_relation=  [col_parent.find_one({"_id": ObjectId( studentdetails['parentid'][0])},{'_id': 0})] #ROLA WALA JAGA    
    roles_relation=studentdetails['role']
    role_relation= [colr.find_one({"_id": ObjectId(roles_relation[0]),'role.0.name':'student'},{'_id': 0})]

    if parent_relation!=None and class_relation !=None :
        studentdetails['parentid'] = (parent_relation)
        studentdetails['class_id'] = class_relation
        studentdetails['role']=role_relation

        col_student.insert_one(studentdetails) # Changing ki hab 
        return True
    return False


    
async def modifystudent(student_id:str , details):
    studentdetails=details
    try:  
        if studentdetails['password']!=None:
            hashed = auth_handler.get_password_hash(details['password'])
            studentdetails['password']=hashed
        else:
            pass

        #### MODIFY Relations 
        class_relation= [col_Class.find_one({"_id": ObjectId( studentdetails['class_id'][0])},{'_id': 0})]
        parent_relation=  [col_parent.find_one({"_id": ObjectId( studentdetails['parentid'][0])},{'_id': 0})] #ROLA WALA JAGA    
        roles_relation=studentdetails['role']
        role_relation= [colr.find_one({"_id": ObjectId(roles_relation[0]),'role.0.name':'student'},{'_id': 0})]

        if role_relation!=None:
            studentdetails['role']=role_relation
        if parent_relation!=None: 
            studentdetails['parentid'] = (parent_relation)
        if class_relation !=None :
            studentdetails['class_id'] = class_relation
    except:
        pass


    col_student.update_one({"_id": ObjectId(student_id)}, {"$set": studentdetails})
    return {"Succesfully updated the record"}

async def deletebyid(student_id:str):
    col_student.delete_one({'_id': ObjectId(student_id)})
    return True
