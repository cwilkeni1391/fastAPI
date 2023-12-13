import pymongo
import os
from dotenv import load_dotenv

load_dotenv()

connectionstring = "mongodb://" + os.getenv("user") + ":" + os.getenv("passw") + "@10.0.0.107:27017"
myclient = pymongo.MongoClient(connectionstring)

mydb = myclient["mydatabase"]

mycol = mydb["persons"]
mydict = {"name": "john","address": "testing ave", "isactive" : False}
mycol.insert_one(mydict)
print(myclient.list_database_names())

for x in mycol.find():
    print(x)