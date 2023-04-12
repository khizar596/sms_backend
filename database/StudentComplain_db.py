from settings import sms_db
from fastapi import HTTPException
from bson import ObjectId
from database.Admin_db import col_Admin
from database.Student_db import col_student
from database.StudentAdmin_db import col_StudentAdmin
# is k andr studnet admin ko complete kr k  dalna ha 
col_Std_comp = sms_db.Std_complain
from models.StudentComplain import StudentComplain



async def viewStd_comp():
    Std_comps=[]
    cursor = col_Std_comp.find({})

    for document in cursor:
        Student_id_check = str(document['Studentid'])
        student_found=  col_student.find_one({"_id": ObjectId(Student_id_check)},{'_id': 0})
        if student_found:
            document['Studentid']=student_found
        else:
            raise ValueError
        StudentAdminid = str(document['StudentAdminid'])
        studentadm_found=  col_StudentAdmin.find_one({"_id": ObjectId(StudentAdminid)},{'_id': 0})
        if studentadm_found:
            document['StudentAdminid']=StudentAdminid
        else:
            raise ValueError
        Std_comps.append((StudentComplain(**document)))
    return Std_comps

async def searchStd_comp(Std_comp_id : str)->dict:

    document=  col_Std_comp.find_one({"_id": ObjectId(Std_comp_id)},{'_id': 0}) 
    
    if not document:

        raise HTTPException(status_code=404, detail="Item not found")
    Student_id_check = str(document['Studentid'])
    student_found=  col_student.find_one({"_id": ObjectId(Student_id_check)},{'_id': 0})
    if student_found:
        document['Studentid']=student_found
    else:
            raise ValueError
    StudentAdminid = str(document['StudentAdminid'])
    studentadm_found=  col_StudentAdmin.find_one({"_id": ObjectId(StudentAdminid)},{'_id': 0})
    if studentadm_found:
        document['StudentAdminid']=StudentAdminid
    else:
            raise ValueError
    return document


async def addStd_comp(details):
    Std_compdetails= details

    Student_id_check = str(Std_compdetails['Studentid'])
    StudentAdminid = str(details['StudentAdminid'])

    studentadm_found=  col_StudentAdmin.find_one({"_id": ObjectId(StudentAdminid)},{'_id': 0})
    Student_id_check = str(details['Studentid'])
    student_found=  col_student.find_one({"_id": ObjectId(Student_id_check)},{'_id': 0})
   
    if student_found!=None and studentadm_found!=None:
        # Std_compdetails['Studentid']=student_found
        col_Std_comp.insert_one(Std_compdetails) 
        return True
    raise LookupError
async def modifyStd_comp(Std_comp_id:str , details):
    col_Std_comp.update_one({"_id": ObjectId(Std_comp_id)}, {"$set": details})
    return {"Succesfully updated the record"}

async def deletebyid(Std_comp_id:str):
    col_Std_comp.delete_one({'_id': ObjectId(Std_comp_id)})
    return True
