from app.repositories.employee_repository import EmployeeRepository
from app.models.employee_model import Employee
from datetime import datetime

class EmployeeService:

    def __init__(self):
        self.repo = EmployeeRepository()

    def create_employee(self, data):
        required_fields = ["name", "email", "department"]

        for field in required_fields:
            if field not in data:
                raise ValueError(f"{field} is required")

        if self.repo.get_by_email(data["email"]):
            raise ValueError("Email already exists")

        employee = Employee(
            name=data["name"],
            email=data["email"],
            department=data["department"],
            date_joined=datetime.strptime(
                data.get("date_joined", datetime.today().strftime("%Y-%m-%d")),
                "%Y-%m-%d"
            )
        )

        return self.repo.create(employee)

    def get_all_employees(self):
        return self.repo.get_all()

    def get_employee(self, emp_id):
        employee = self.repo.get_by_id(emp_id)
        if not employee:
            raise ValueError("Employee not found")
        return employee

    def update_employee(self, emp_id, data):
        employee = self.get_employee(emp_id)

        employee.name = data.get("name", employee.name)
        employee.department = data.get("department", employee.department)
        employee.date_joined = data.get("date_joined", employee.date_joined)

        self.repo.update()
        return employee

    def delete_employee(self, emp_id):
        employee = self.get_employee(emp_id)
        self.repo.delete(employee)
