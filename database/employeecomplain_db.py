from settings import sms_db
from fastapi import HTTPException
from bson import ObjectId
col_Emp_comp = sms_db.Emp_complain
from models.EmployeeComplain import EmployeeComplain



async def viewEmp_comp():
    Emp_comps=[]
    cursor = col_Emp_comp.find({})

    for document in cursor:
        document['_id']=str(document['_id'])

        Emp_comps.append(document)
    return Emp_comps

# async def searchEmp_comp(Emp_comp_id : str)->dict:

#     document=  col_Emp_comp.find_one({"_id": ObjectId(Emp_comp_id)},{'_id': 0}) 
    
#     if not document:

#         raise HTTPException(status_code=404, detail="Item not found")
    
#     return document


async def addEmp_comp(details):
    Emp_compdetails= details
    
    col_Emp_comp.insert_one(Emp_compdetails) # Changing ki hab 
    return True

async def modifyEmp_comp(Emp_comp_id:str , details):
    col_Emp_comp.update_one({"_id": ObjectId(Emp_comp_id)}, {"$set": details})
    return {"Succesfully updated the record"}

async def deletebyid(Emp_comp_id:str):
    col_Emp_comp.delete_one({'_id': ObjectId(Emp_comp_id)})
    return True
