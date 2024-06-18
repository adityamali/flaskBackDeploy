# external imports
from flask import Flask, jsonify, request
from flask_cors import CORS

from services.employeeServices import Employee
from services.auth import Auth

app = Flask(__name__)
CORS(app)


@app.route('/')
def home():
    return "hello"


@app.route('/api/stamp/<name>', methods=['POST'])
def punch_controller(name):
    empx = Employee(empMail="", empName=name, empPhone=0)
    res = empx.PunchProvider()
    return jsonify(res)


@app.route('/api/login/email=<email>&pass=<password>', methods=['POST'])
def auth_controller(email, password):
    # print("recieved:" + email + password)
    auth0 = Auth(email0=email, password0=password)
    x = auth0.authenticate()
    return jsonify(x)


@app.route('/api/employees', methods=['GET'])
def emp_provider():
    try:
        emps = Employee(empName="", empPhone="", empMail="")
        x = emps.EmpProvider()
        return jsonify(x), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/api/add', methods=['POST'])
def new_emp():
    # Assuming JSON data is sent in the request body
    data = request.json
    name = data.get('name')
    phone = data.get('phone')
    email = data.get('email')

    # Basic validation
    if not all([name, phone, email]):
        return jsonify({"error": "Missing name, phone, or email"}), 400
    
    emp = Employee(empName=name, empPhone=phone, empMail=email)
    emp.AddEmp()

    print(name, phone, email)
    return jsonify({"name": name, "phone": phone, "email": email}), 200



if __name__ == '__main__':
   app.run(debug=True)