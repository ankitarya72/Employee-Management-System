from unittest.mock import MagicMock

# ================= CREATE EMPLOYEE =================

# SUCCESS case
def test_create_employee_success(client, mocker):
    mock_employee = MagicMock()
    mock_employee.to_dict.return_value = {
        "id": 1,
        "name": "Ankit",
        "email": "ankit@gmail.com",
        "department": "IT",
        "date_joined": "2025-01-01"
    }

    mocker.patch(
        "app.controllers.employee_controller.service.create_employee",
        return_value=mock_employee
    )

    payload = {
        "name": "Ankit",
        "email": "ankit@gmail.com",
        "department": "IT"
    }

    response = client.post("/employees", json=payload)

    assert response.status_code == 201
    assert response.json["name"] == "Ankit"


# ERROR case
def test_create_employee_error(client, mocker):
    mocker.patch(
        "app.controllers.employee_controller.service.create_employee",
        side_effect=ValueError("Email already exists")
    )

    payload = {
        "name": "Ankit",
        "email": "ankit@gmail.com",
        "department": "IT"
    }

    response = client.post("/employees", json=payload)

    assert response.status_code == 400
    assert response.json["error"] == "Email already exists"


# ================= GET ALL EMPLOYEES =================

def test_get_employees_success(client, mocker):
    emp1 = MagicMock()
    emp1.to_dict.return_value = {
        "id": 1,
        "name": "Ankit",
        "email": "ankit@gmail.com",
        "department": "IT",
        "date_joined": "2025-01-01"
    }

    emp2 = MagicMock()
    emp2.to_dict.return_value = {
        "id": 2,
        "name": "Richa",
        "email": "richa@gmail.com",
        "department": "HR",
        "date_joined": "2025-01-02"
    }

    mocker.patch(
        "app.controllers.employee_controller.service.get_all_employees",
        return_value=[emp1, emp2]
    )

    response = client.get("/employees")

    assert response.status_code == 200
    assert len(response.json) == 2
    assert response.json[0]["name"] == "Ankit"


# ================= GET EMPLOYEE =================

def test_get_employee_success(client, mocker):
    mock_employee = MagicMock()
    mock_employee.to_dict.return_value = {
        "id": 1,
        "name": "Ankit",
        "email": "ankit@gmail.com",
        "department": "IT",
        "date_joined": "2025-01-01"
    }

    mocker.patch(
        "app.controllers.employee_controller.service.get_employee",
        return_value=mock_employee
    )

    response = client.get("/employees/1")

    assert response.status_code == 200
    assert response.json["name"] == "Ankit"


def test_get_employee_not_found(client, mocker):
    mocker.patch(
        "app.controllers.employee_controller.service.get_employee",
        side_effect=ValueError("Employee not found")
    )

    response = client.get("/employees/999")

    assert response.status_code == 400
    assert response.json["error"] == "Employee not found"


# ================= UPDATE EMPLOYEE =================

def test_update_employee_success(client, mocker):
    mock_employee = MagicMock()
    mock_employee.to_dict.return_value = {
        "id": 1,
        "name": "Ankit Updated",
        "email": "ankit@gmail.com",
        "department": "IT",
        "date_joined": "2025-01-01"
    }

    mocker.patch(
        "app.controllers.employee_controller.service.update_employee",
        return_value=mock_employee
    )

    response = client.put("/employees/1", json={"name": "Ankit Updated"})

    assert response.status_code == 200
    assert response.json["name"] == "Ankit Updated"


def test_update_employee_error(client, mocker):
    mocker.patch(
        "app.controllers.employee_controller.service.update_employee",
        side_effect=ValueError("Employee not found")
    )

    response = client.put("/employees/999", json={"name": "Ankit Updated"})

    assert response.status_code == 400
    assert response.json["error"] == "Employee not found"


# ================= DELETE EMPLOYEE =================

def test_delete_employee_success(client, mocker):
    mocker.patch(
        "app.controllers.employee_controller.service.delete_employee",
        return_value=None
    )

    response = client.delete("/employees/1")

    assert response.status_code == 200
    assert response.json["message"] == "Employee deleted"


def test_delete_employee_not_found(client, mocker):
    mocker.patch(
        "app.controllers.employee_controller.service.delete_employee",
        side_effect=ValueError("Employee not found")
    )

    response = client.delete("/employees/999")

    assert response.status_code == 400
    assert response.json["error"] == "Employee not found"
