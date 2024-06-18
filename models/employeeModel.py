import datetime

class Employee:
    employeeID = ""
    employeeName = ""
    employeePhone = ""

    def __init__(self, empID, empName, empPhone) -> None:
        self.employeeID = empID
        self.employeeName = empName
        self.employeePhone = empPhone



