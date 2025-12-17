from app.services.employee_service import EmployeeService
from unittest.mock import MagicMock
import pytest
from datetime import date

# ================= CREATE EMPLOYEE =================

def test_create_employee_success():
    service = EmployeeService()

    # mock repository methods
    service.repo = MagicMock()
    service.repo.get_by_email.return_value = None
    service.repo.create.return_value = "EMPLOYEE_CREATED"

    data = {
        "name": "Ankit",
        "email": "ankit@gmail.com",
        "department": "IT"
    }

    result = service.create_employee(data)

    assert result == "EMPLOYEE_CREATED"
    service.repo.get_by_email.assert_called_once_with("ankit@gmail.com")
    service.repo.create.assert_called_once()


def test_create_employee_missing_field():
    service = EmployeeService()

    data = {
        "email": "ankit@gmail.com",
        "department": "IT"
    }

    with pytest.raises(ValueError) as exc:
        service.create_employee(data)

    assert str(exc.value) == "name is required" 


def test_create_employee_duplicate_email():
    service = EmployeeService()

    service.repo = MagicMock()
    service.repo.get_by_email.return_value = True

    data = {
        "name": "Ankit",
        "email": "ankit@gmail.com",
        "department": "IT"
    }

    with pytest.raises(ValueError) as exc:
        service.create_employee(data)

    assert str(exc.value) == "Email already exists"


# ================= GET ALL EMPLOYEES =================

def test_get_all_employees_success():
    service = EmployeeService()

    # mock repository
    service.repo = MagicMock()
    service.repo.get_all.return_value = ["emp1", "emp2"]

    result = service.get_all_employees()

    assert result == ["emp1", "emp2"]
    service.repo.get_all.assert_called_once()

# ================= GET EMPLOYEE BY ID =================

def test_get_employee_success():
    service = EmployeeService()

    # mock repository
    service.repo = MagicMock()
    fake_employee = {"id": 1, "name": "Ankit"}
    service.repo.get_by_id.return_value = fake_employee

    result = service.get_employee(1)

    assert result == fake_employee
    service.repo.get_by_id.assert_called_once_with(1)


def test_get_employee_not_found():
    service = EmployeeService()

    # mock repository
    service.repo = MagicMock()
    service.repo.get_by_id.return_value = None

    with pytest.raises(ValueError, match="Employee not found"):
        service.get_employee(99)

# ================= UPDATE EMPLOYEE =================

def test_update_employee_success():
    service = EmployeeService()

    # fake employee object
    fake_employee = MagicMock()
    fake_employee.name = "Old Name"
    fake_employee.department = "Old Dept"
    fake_employee.date_joined = date(2024, 1, 1)

    # mock methods
    service.get_employee = MagicMock(return_value=fake_employee)
    service.repo = MagicMock()

    data = {
        "name": "New Name",
        "department": "IT"
    }

    result = service.update_employee(1, data)

    # assertions
    assert result.name == "New Name"
    assert result.department == "IT"
    assert result.date_joined == date(2024, 1, 1)  # unchanged
    service.repo.update.assert_called_once()

# ================= DELETE EMPLOYEE =================

def test_delete_employee_success():
    service = EmployeeService()

    fake_employee = MagicMock()

    # mock get_employee
    service.get_employee = MagicMock(return_value=fake_employee)

    # mock repository
    service.repo = MagicMock()

    service.delete_employee(1)

    # assertions
    service.get_employee.assert_called_once_with(1)
    service.repo.delete.assert_called_once_with(fake_employee)
