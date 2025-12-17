from app.models.employee_model import Employee
from app.database import db

class EmployeeRepository:

    def create(self, employee):
        db.session.add(employee)
        db.session.commit()
        return employee

    def get_all(self):
        return Employee.query.all()

    def get_by_id(self, emp_id):
        return Employee.query.get(emp_id)

    def get_by_email(self, email):
        return Employee.query.filter_by(email=email).first()

    def update(self):
        db.session.commit()

    def delete(self, employee):
        db.session.delete(employee)
        db.session.commit()
