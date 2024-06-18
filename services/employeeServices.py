from bson import json_util
import json
import datetime
from repo.connector import Connector

mongo = Connector()

class Employee:
    employeeName = ""
    employeePhone = ""
    employeeMail = ""
    entry = []


    def __init__(self, empName, empPhone, empMail) -> None:
        time = str(datetime.datetime.now())
        self.employeeName = empName
        self.employeePhone = empPhone
        self.employeeMail = empMail
        self.entry = [time]

    def PunchProvider(self):
        # employee = mongo.employeeCol.find_one({"empName": self.employeeName})
        time = str(datetime.datetime.now())
        employee = mongo.employeeCol.find_one_and_update({"empName": self.employeeName}, {"$push": {"entry": time}})
        x = json.loads(json_util.dumps(employee))
        return x
    
    def EmpProvider(self):
        employees = list(mongo.employeeCol.find({}))
        return json.loads(json_util.dumps(employees))
    
    def AddEmp(self):
        time = str(datetime.datetime.now())
        mongo.employeeCol.insert_one({"empName": self.employeeName, "empPhone": self.employeePhone, "empMail": self.employeeMail, "entry" : [time]})