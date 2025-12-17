from flask import Blueprint, request, jsonify
from app.services.employee_service import EmployeeService

employee_bp = Blueprint("employee_bp", __name__)
service = EmployeeService()

@employee_bp.route("/employees", methods=["POST"])
def create_employee():
    employee = service.create_employee(request.json)
    return jsonify(employee.to_dict()), 201

@employee_bp.route("/employees", methods=["GET"])
def get_employees():
    employees = service.get_all_employees()
    return jsonify([emp.to_dict() for emp in employees])

@employee_bp.route("/employees/<int:emp_id>", methods=["GET"])
def get_employee(emp_id):
    employee = service.get_employee(emp_id)
    return jsonify(employee.to_dict())

@employee_bp.route("/employees/<int:emp_id>", methods=["PUT"])
def update_employee(emp_id):
    employee = service.update_employee(emp_id, request.json)
    return jsonify(employee.to_dict())

@employee_bp.route("/employees/<int:emp_id>", methods=["DELETE"])
def delete_employee(emp_id):
    service.delete_employee(emp_id)
    return jsonify({"message": "Employee deleted"})
