# from models.Users_login import AuthDetails
from fastapi import HTTPException
import jwt
from fastapi.security import HTTPAuthorizationCredentials ,HTTPBearer 
from fastapi import Security
from passlib.context import CryptContext
from datetime import datetime,timedelta



class AuthHandler():
    security = HTTPBearer()
    pwd_context = CryptContext(schemes=["bcrypt"], deprecated = "auto") #CHECK IT IF ANY ERROR
    secret = 'gcfvxEbmtYf4IvtjDDV7YuWQXcE'

    def get_password_hash(self, password):
        return self.pwd_context.hash(password)
    
    def verify_password(self, plain_password, hashed_password):
        return self.pwd_context.verify(plain_password,hashed_password)

    def encode_token(self,user_id):
        # user_id['_id']=JSONEncoder().encode(user_id['_id'])
        user_id['_id']=str(user_id['_id'])
        payload= { 
            "exp": datetime.utcnow()  + timedelta( days= 0, minutes = 5),
            "iat": datetime.now(),
            "details" : user_id
        }

        return jwt.encode(
            payload,
            self.secret,
            algorithm = "HS256"
        ),user_id


    def decode_token(self, token):
        try:
            payload= jwt.decode(token, self.secret, algorithms =['HS256'])
            return payload['details']
        except jwt.ExpiredSignatureError:
            raise HTTPException( status_code=401 , detail= "Signature has expired ")
        except jwt.InvalidTokenError as e :
            raise HTTPException( status_code=401, detail= "Invalid token ")

    def auth_wrapper( self, auth : HTTPAuthorizationCredentials = Security(security)):
        return self.decode_token(auth.credentials)


import json
from bson import ObjectId

class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        return json.JSONEncoder.default(self, o)






# async def Authdetails(details):
#     userlogindetails= details
#     cursor = col_userlogin.find({})

#     for document in cursor:
#         if document['cnic']==userlogindetails['cnic']:
#             response= {"CNIC " : "already exist "}
#             return response
#         elif document['email']==userlogindetails['email']:
#             response={"Email " : "already exist "}    
#             return response
#     col_userlogin.insert_one(userlogindetails) # Changing ki hab 
#     return True

