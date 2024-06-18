from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import os

class Connector:
    uri = "mongodb+srv://Cluster45343:ZU9gUV9DelNC@cluster45343.ykd6owm.mongodb.net/?retryWrites=true&w=majority&appName=Cluster45343"
    client = MongoClient(uri, server_api=ServerApi('1'))
    employeeDB = client['IndustryAI_employeeManager']

    employeeCol = employeeDB["employees"]

    

# # Send a ping to confirm a successful connection
# try:
#     client.admin.command('ping')
#     print("Pinged your deployment. You successfully connected to MongoDB!")
# except Exception as e:
#     print(e)


# empx = Connector()

# try:
#     res = empx.employeeCol.find_one({"empName": "Satyam"})
    
#     if res:
#         print(f"{res} is con test res")
#     else:
#         print("No document found with empName 'Tom'")
# except Exception as e:
#     print(e)
