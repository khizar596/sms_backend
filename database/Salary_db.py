from settings import sms_db
from fastapi import HTTPException
from models.Salary2 import Salary2
from database.employeecomplain_db import cole ,col_Admin
from bson import ObjectId
col_Salary = sms_db.Salary



async def viewSalary():
    col_Salarys=[]
   
    cursor = col_Salary.find({})
   
    for document in cursor:
        try:
            Employee2id_relation=  cole.find_one({"_id": ObjectId( document['Employee2id'])},{'_id': 0,'first_name':1})
            print(Employee2id_relation)

        except:
            raise HTTPException(204,"student admin not found")       
        try:
            Admin2id_relation = col_Admin.find_one({"_id": ObjectId(document['Admin2id']), 'role.0.name': 'Admin'}, {'_id': 0,'name':1})

        except:
            raise HTTPException(204,"Admin not found")
        try:
            Accountant2id_relation = cole.find_one({"_id": ObjectId(document['Accountant2id']),'role.0.name': 'Accountant'}, {'_id': 0,'first_name':1})

        except:
            raise HTTPException(204,"Accountant not found")
        if Employee2id_relation and Admin2id_relation and Accountant2id_relation:
            document['Admin2id'] = Admin2id_relation
            document['Employee2id'] = Employee2id_relation 
            document['Accountant2id'] = Accountant2id_relation 
            document['_id']= str(document['_id'])        
            col_Salarys.append(document)
        
    return col_Salarys
    

async def searchSalary(Salary_id : str)->dict:

    document=  col_Salary.find_one({"_id": ObjectId(Salary_id)},{'_id': 0}) 
    
    if not document:

        raise HTTPException(status_code=404, detail="document not found")
    try:
        Employee2id_relation=  cole.find_one({"_id": ObjectId( document['Employee2id'])},{'_id': 0,'first_name':1})
        print(Employee2id_relation)

    except:
        raise HTTPException(204,"student admin not found")       
    try:
        Admin2id_relation = col_Admin.find_one({"_id": ObjectId(document['Admin2id']), 'role.0.name': 'Admin'}, {'_id': 0,'name':1})

    except:
        raise HTTPException(204,"Admin not found")
    try:
        Accountant2id_relation = cole.find_one({"_id": ObjectId(document['Accountant2id']),'role.0.name': 'Accountant'}, {'_id': 0,'first_name':1})

    except:
        raise HTTPException(204,"Accountant not found")
    if Employee2id_relation and Admin2id_relation and Accountant2id_relation:
        document['Admin2id'] = Admin2id_relation
        document['Employee2id'] = Employee2id_relation 
        document['Accountant2id'] = Accountant2id_relation 
    return document


async def addSalary(details):
    if  "Employee2id" in details:
        try:
            Employee2id_relation=  cole.find_one({"_id": ObjectId( details['Employee2id'])},{'_id': 0})
        except:
            raise HTTPException(204,"student admin not found")
        if Employee2id_relation==None:
            raise HTTPException(204, detail="check your Employee id")

    if "Admin2id" in details:
        try:
            Admin2id_relation = col_Admin.find_one({"_id": ObjectId(details['Admin2id']), 'role.0.name': 'Admin'}, {'_id': 0,'name':1})
        except:
            raise HTTPException(204,"Admin not found")
        
        if Admin2id_relation==None:
            raise HTTPException(204, detail="check your Admin id")
    if "Accountant2id" in details:
        try:
            Accountant2id_relation = cole.find_one({"_id": ObjectId(details['Accountant2id']), 'role.0.name': 'Accountant'}, {'_id': 0,'name':1})
        except:
            raise HTTPException(204,"Admin not found")
        
        if Accountant2id_relation==None:
            raise HTTPException(204, detail="check your Admin id")


    col_Salary.insert_one(details) 

async def modifySalary(Salary_id:str , details):
    if  "Employee2id" in details:
        Employee2id_relation=  cole.find_one({"_id": ObjectId( details['Employee2id'])},{'_id': 0})
        if Employee2id_relation==None:
            del details['Employee2id']
    if "Admin2id" in details:
        Admin2id_relation = col_Admin.find_one({"_id": ObjectId(details['Admin2id']), 'role.0.name': 'Admin'}, {'_id': 0,'name':1})
        if Admin2id_relation==None:
            del details['Admin2id']
    if "Accountant2id" in details:
        Accountant2id_relation = col_Admin.find_one({"_id": ObjectId(details['Accountant2id']), 'role.0.name': 'Admin'}, {'_id': 0,'name':1})
        if Accountant2id_relation==None:
            del details['Accountant2id']
    col_Salary.update_one({"_id": ObjectId(Salary_id)}, {"$set": details})
    return {"Succesfully updated the record"}

async def deleteSalaryid(Salary_id:str):
    col_Salary.delete_one({'_id': ObjectId(Salary_id)})
    return True
