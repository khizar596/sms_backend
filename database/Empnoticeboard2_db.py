from settings import sms_db
from bson import ObjectId
from models.EmployeeNoticeboard2 import Emp_noticeboard
col_empnotice = sms_db.Emp_Noticeboard



async def viewempnotice():
    empnotices=[]
    cursor = col_empnotice.find({})

    for document in cursor:
        empnotices.append((Emp_noticeboard(**document)))
    return empnotices

# async def searchempnotice(empnotice_id : str)->dict:

#     document=  col_empnotice.find_one({"_id": ObjectId(empnotice_id)},{'_id': 0}) 
    
#     if not document:

#         raise HTTPException(status_code=404, detail="document not found")
    
#     return document


async def addempnotice(details):
    empnoticedetails= details
    
    col_empnotice.insert_one(empnoticedetails) 
    return True

async def modifyempnotice(empnotice_id:str , details):
    col_empnotice.update_one({"_id": ObjectId(empnotice_id)}, {"$set": details})
    return {"Succesfully updated the record"}

async def deleteempnoticeid(empnotice_id:str):
    col_empnotice.delete_one({'_id': ObjectId(empnotice_id)})
    return True
