from settings import sms_db
from bson import ObjectId
from models.StudentNoticeboard import StudentNoticeboard   
col_stdnotice = sms_db.Student_Noticeboard
from database.Admin_db import col_Admin
from database.StudentAdmin_db import col_StudentAdmin


async def viewstdnotice():
    stdnotices=[]
    cursor = col_stdnotice.find({})

    for document in cursor:
        stdnotices.append((StudentNoticeboard(**document)))
    return stdnotices

# async def searchstdnotice(stdnotice_id : str)->dict:

#     document=  col_stdnotice.find_one({"_id": ObjectId(stdnotice_id)},{'_id': 0}) 
    
#     if not document:

#         raise HTTPException(status_code=404, detail="document not found")
    
#     return document


async def addstdnotice(details):
    stdnoticedetails= details
    Admin_relation=  [col_Admin.find_one({"_id": ObjectId( stdnoticedetails['Admin2id'][0])},{'_id': 0})]
    StdAdmin_relation=  [col_StudentAdmin.find_one({"_id": ObjectId( stdnoticedetails['StudentAdminid'][0])},{'_id': 0})]
    if Admin_relation and StdAdmin_relation:
        # stdnoticedetails['Admin2id'] = Admin_relation
        # stdnoticedetails['StudentAdminid'] = StdAdmin_relation
        col_stdnotice.insert_one(stdnoticedetails) 
        return True

async def modifystdnotice(stdnotice_id:str , details):
    col_stdnotice.update_one({"_id": ObjectId(stdnotice_id)}, {"$set": details})
    return {"Succesfully updated the record"}

async def deletestdnoticeid(stdnotice_id:str):
    col_stdnotice.delete_one({'_id': ObjectId(stdnotice_id)})
    return True
