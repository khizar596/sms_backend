import pymongo


config = dotenv_values(".env") 

password= "khizar0405"
Username= "SMKhizar"
secret_key="gcfvxEbmtYf4IvtjDDV7YuWQXcE"
algorithm = "HS256"



SMS=pymongo.MongoClient(f"mongodb+srv://{Username}:{password}@cluster0.v438msx.mongodb.net/?retryWrites=true&w=majority")
# SMS = pymongo.MongoClient(
#     "mongodb+srv://config['USER_NAME_DB']:config['PASSWORD_DB']@cluster0.v438msx.mongodb.net/?retryWrites=true&w=majority")


sms_db = SMS.SMS_DB



# from pydantic import BaseSettings


# class Settings(BaseSettings):
#     DATABASE_URL: str
#     MONGO_INITDB_DATABASE: str

#     JWT_PUBLIC_KEY: str
#     JWT_PRIVATE_KEY: str
#     REFRESH_TOKEN_EXPIRES_IN: int
#     ACCESS_TOKEN_EXPIRES_IN: int
#     JWT_ALGORITHM: str

#     CLIENT_ORIGIN: str

#     class Config:
#         env_file = './.env'


# settings = Settings()
