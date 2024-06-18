from repo.connector import Connector
from bson import json_util
import json

mongo = Connector()

class Auth:
    adminMail = ""
    adminPass = ""

    def __init__(self, email0, password0) -> None:
        self.adminMail = email0
        self.adminPass = password0


    def authenticate(self):
        dbmail = mongo.employeeDB.admin.find_one({"mail": self.adminMail})
        x= dict(dbmail)
        if (self.adminPass == x['password']):
            x = json.loads(json_util.dumps(x))
            return x


    