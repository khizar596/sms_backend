from settings import sms_db
from fastapi import HTTPException
from models.chatbox import Chatbox
from bson import ObjectId
col_chatbox = sms_db.chatbox



async def viewchatbox():
    col_chatboxs=[]
   
    cursor = col_chatbox.find({})
   
    for document in cursor:
        col_chatboxs.append((Chatbox(**document)))
    return col_chatboxs
    

async def searchchatbox(chatbox_id : str)->dict:

    document=  col_chatbox.find_one({"_id": ObjectId(chatbox_id)},{'_id': 0}) 
    
    if not document:

        raise HTTPException(status_code=404, detail="document not found")
    
    return document


async def addchatbox(details):
    chatboxdetails= details
    # feedetails= details
    # Student_id_check = feedetails['Studentid']
    # document=  col_student.find_one({"_id": ObjectId(Student_id_check)},{'_id': 0})    
    # if document:
    #     col_fee.insert_one(feedetails) # Changing ki hab 
    #     return True
    # return {"Id error":"Id of student doesn't exist"}

    col_chatbox.insert_one(chatboxdetails) # Changing ki hab 
    return True

async def modifychatbox(chatbox_id:str , details):
    col_chatbox.update_one({"_id": ObjectId(chatbox_id)}, {"$set": details})
    return {"Succesfully updated the record"}

async def deletechatboxid(chatbox_id:str):
    col_chatbox.delete_one({'_id': ObjectId(chatbox_id)})
    return True
