# from models.Users_login import AuthDetails
from fastapi import HTTPException,Depends
import jwt
from fastapi.security import HTTPAuthorizationCredentials ,HTTPBearer 
from fastapi import Security
from passlib.context import CryptContext
from datetime import datetime,timedelta
from bson import ObjectId
from database.Employee_role_db import col_Employee_role as colr

class AuthHandler():
    security = HTTPBearer()
    pwd_context = CryptContext(schemes=["bcrypt"], deprecated = "auto") #CHECK IT IF ANY ERROR
    secret = 'gcfvxEbmtYf4IvtjDDV7YuWQXcE'
    algorithm="HS256"
    def get_password_hash(self, password):
        return self.pwd_context.hash(password)
    
    def verify_password(self, plain_password, hashed_password):
        return self.pwd_context.verify(plain_password,hashed_password)

    def encode_token(self,user_id):

        # user_id['_id']=JSONEncoder().encode(user_id['_id'])
        user_id['_id']=str(user_id['_id'])
        payload= { 
            "iat": datetime.utcnow() ,
            "exp": datetime.utcnow()  + timedelta( days= 1, minutes = 0),

            "details" : user_id
        }

        return jwt.encode(
            payload,
            self.secret,
            algorithm="HS256",
        ), user_id


    def decode_token(self, token):
        payload = jwt.decode(token, self.secret, algorithms=[self.algorithm])
        # print(payload)
        try:
            
            payload = jwt.decode(token, self.secret, algorithms=[self.algorithm])
            return payload['details']
        except jwt.ExpiredSignatureError:
            raise HTTPException( status_code=401 , detail= "Signature has expired ")
        except jwt.InvalidTokenError as e :
            raise HTTPException( status_code=401, detail= "Invalid token ")

    def auth_wrapper(self, auth : HTTPAuthorizationCredentials = Security(security)):
        # print(auth.credentials)
        return self.decode_token(auth.credentials)

    def has_permission(self, user, permission):
        if user['role'][0]['name'] == 'Parent':
            
            if permission in [
                'search_quizz', 'search_fee', 'search_assignment','search_datesheet','search_stdattendence'
                'search_timetable','search_marksheet','search_student'
                'view_subject'
                ]:
                return True
            
        elif user['role'][0]['name']  == 'Admin':
            if permission in [
                'search_student','add_student', 'modify_student','view_student','delete_student',
                'search_stdcomp','add_stdcomp', 'modify_stdcomp','view_stdcomp','delete_stdcomp',
                'search_parent','add_parent', 'modify_parent','view_parent','delete_parent',
                'search_accountant','add_accountant', 'modify_accountant','view_accountant','delete_accountant',
                'search_subject','add_subject', 'modify_subject','view_subject','delete_subject',
                'search_staff','add_staff', 'modify_staff','view_staff','delete_staff',
                'search_stdnotic','add_stdnotic', 'modify_stdnotic','view_stdnotic','delete_stdnotic',
                'search_stdattendence','add_stdattendence', 'modify_stdattendence','view_stdattendence','delete_stdattendence',
                'search_course','add_course', 'modify_course','view_course','delete_course',
                'search_class','add_class', 'modify_class','view_class','delete_class',
                'search_section','add_section', 'modify_section','view_section','delete_section',
                'search_timetable','add_timetable', 'modify_timetable','view_timetable','delete_timetable',
                'search_chatbox','add_chatbox', 'modify_chatbox','view_chatbox','delete_chatbox',
                'search_Quiz','add_Quiz', 'modify_Quiz','view_Quiz','delete_Quiz',
                'search_assignment','add_assignment', 'modify_assignment','view_assignment','delete_assignment',
                'search_exam','add_exam', 'modify_exam','view_exam','delete_exam',
                'search_datesheet','add_datesheet', 'modify_datesheet','view_datesheet','delete_datesheet',
                'search_marksheet','add_marksheet', 'modify_marksheet','view_marksheet','delete_marksheet',
                'search_empnotic','add_empnotic', 'modify_empnotic','view_empnotic','delete_empnotic',
                'search_empattendence','add_empattendence', 'modify_empattendence','view_empattendence','delete_empattendence',
                'search_empcomp','add_empcomp', 'modify_empcomp','view_empcomp','delete_empcomp',
                'search_salary','add_salary', 'modify_salary','view_salary','delete_salary',
                'search_employee','add_employee', 'modify_employee','view_employee','delete_employee'
                ]:
                return True
            
        elif user['role'][0]['name']  == 'Exam Admin':
            if permission in [
                'search_subject','add_subject', 'modify_subject','view_subject','delete_subject'
                'view_empnotic','search_empnotic','view_empattendence', 'modify_empcomp','view_empcomp','search_salary',
                'search_quizz','add_quizz', 'modify_quizz','view_quizz','delete_quizz'
                'search_assignment','add_assignment', 'modify_assignment','view_assignment','delete_assignment'
                'search_exam','add_exam', 'modify_exam','view_exam','delete_exam',
                'search_datesheet','add_datesheet', 'modify_datesheet','view_datesheet','delete_datesheet',
                'add_marksheet',
                ]:
                
                return True 
        elif user['role'][0]['name']  == 'Accountant':
            if permission in [
                'view_empnotic', 'view_attendenceReport','add_empcomp','modify_empcomp','add_salary','modify_salary','add_fee','modify_fee']:
                return True

            
        elif user['role'][0]['name']  == 'HR':
            if permission in [
                'view_empnotic', 'add_empnotic','modify_empnotic',
                'view_salary','view_empcomp',
                'search_employee','add_employee', 'modify_employee','view_employee','delete_employee'

                ]:
                return True    
            
            
            
            
            
            
            
        elif user['role'][0]['name']  == 'Student Admin':
            if permission in [
                'search_parent','add_parent', 'modify_parent','view_parent','delete_parent',
                'search_student','add_student', 'modify_student','view_student','delete_student',
                'view_stdcomp',
                'search_stdnotic','add_stdnotic', 'modify_stdnotic','view_stdnotic','delete_stdnotic',
                'search_stdattendence','add_stdattendence', 'modify_stdattendence','view_stdattendence','delete_stdattendence',
                'search_course','add_course', 'modify_course','view_course','delete_course',
                'search_class','add_class', 'modify_class','view_class','delete_class',
                'search_subject','add_subject', 'modify_subject','view_subject','delete_subject',

                'search_section','add_section', 'modify_section','view_section','delete_section',
                'search_timetable','add_timetable', 'modify_timetable','view_timetable','delete_timetable',
                'search_chatbox','add_chatbox', 'modify_chatbox','view_chatbox','delete_chatbox',
                
                              ]:
                return True
           
            
        elif user['role'][0]['name']  == 'Staff':
                    if permission in [
                        'view_empnotic', 'view_empattendence','view_attendenceReport',
                        'add_empcomp', 'modify_empcomp','view_empcomp','view_salary'

                        ]:
                        return True
                    
                   



        elif user['role'][0]['name']  == 'Teacher':
            if permission in [
                'view_empnotic', 'view_empattendence','add_empcomp','modify_empcomp',
                'view_salary','add_quizz','add_assignment',
                'view_exam',
                'view_datesheet',
                'view_stdnotic','add_stdattendence','modify_stdattendence','view_course',
                'view_class','view_section','view_timetable','chatbox'
                'view_subject'
                ]:
                return True
            
            
            
        elif user['role'][0]['name']  == 'Student':
            if permission in [
                                'add_student', 'modify_student','view_student','view_fee',
                                'solve_quiz',
                                'upload_assignment',
                                'view_exam','view_datesheet','view_marksheet',
                                'view_stdnotic',
                                'view_attendencereport',
                                'view_course',
                                'view_class',
                                'view_section',
                                'view_timetable',
                                'chatbox'

                              ]:
                return True







        raise HTTPException(status_code=403, detail="Not enough permissions")






async def registration(details,cole,colr):
    employeedetails= details

    employe_role=employeedetails['role']
    role_relation= [colr.find_one({"_id": ObjectId(employe_role[0])},{'_id': 0})]

    cursor = cole.find({},{"_id":0})    

    for document in cursor:
        if document['cnic']==employeedetails['cnic']:
            raise HTTPException( status_code=401, detail= "Cnic exist")

        elif document['email']==employeedetails['email']:
            raise HTTPException( status_code=401, detail= "Email exist")
    auth_handler=AuthHandler()
    hashed = auth_handler.get_password_hash(employeedetails['password'])
    employeedetails['password']=hashed
    
    if role_relation:
        employeedetails['role']=role_relation
        cole.insert_one(employeedetails) 
        return True
        
    raise HTTPException( status_code=401, detail= "Role is not defined")
