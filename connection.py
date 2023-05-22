# import os
# from dotenv import load_dotenv
from pymongo import MongoClient

# MONGODB_URI = os.environ['MONGODB_URI']
MONGODB_URI = "mongodb+srv://myAtlasDBUser:12345@myatlasclusteredu.uxcjrlj.mongodb.net/?retryWrites=true&w=majority"

client = MongoClient(MONGODB_URI)

for db_name in client.list_database_names(): print(db_name)

