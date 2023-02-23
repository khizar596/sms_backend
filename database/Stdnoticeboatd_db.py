from settings import sms_db
from bson import ObjectId
from models.StudentNoticeboard import StudentNoticeboard   
col_stdnotice = sms_db.Student_Noticeboard



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
    
    col_stdnotice.insert_one(stdnoticedetails) 
    return True

async def modifystdnotice(stdnotice_id:str , details):
    col_stdnotice.update_one({"_id": ObjectId(stdnotice_id)}, {"$set": details})
    return {"Succesfully updated the record"}

async def deletestdnoticeid(stdnotice_id:str):
    col_stdnotice.delete_one({'_id': ObjectId(stdnotice_id)})
    return True
