# Employee Management System (EMS)

## Project Overview
This is a **Employee Management System** built using **Python**, **Flask**, and **MySQL**.  
The project follows a **layered architecture**, making it easy to understand and maintain:

1. **Controller (Routes):** Defines Flask API endpoints to create, read, update, and delete employees, and delegates all business logic to the `EmployeeService`.  
2. **Service:** Contains the business logic for validating employee data and handling CRUD operations using the repository.  
3. **Repository:** Handles all database operations (CRUD) for employees using SQLAlchemy.  
4. **Models:** Defines the Employee database table structure and provides a method to convert employee data into a dictionary for API responses.  
5. **Global Exception Handling:** Catches errors globally, eliminating the need for `try-except` in every API.  
6. **Unit Tests:** Ensures the code works as expected.  

---

## Prerequisites

Make sure you have the following installed:

- **Python 3.10+**: [Download Python](https://www.python.org/downloads/)  
- **MySQL**: [Install MySQL](https://dev.mysql.com/downloads/)  
- **VS Code** (or any code editor)  
- **Postman**: [Download Postman](https://www.postman.com/downloads/)  

---

## Project Setup

### 1. Clone the repository
```bash
git clone <your-repo-url>
cd employee-management
2. Install dependencies
bash
Copy code
pip install -r requirements.txt
3. Configure the database
Open MySQL.

Create a database:

sql
Copy code
CREATE DATABASE ems_db;
Update your database configuration in app/database.py:

python
Copy code
DB_USER = "your_username"
DB_PASSWORD = "your_password"
DB_HOST = "localhost"
DB_NAME = "ems_db"
Project Structure
graphql
Copy code
employee-management/
│
├── app/
│   ├── controllers/        # Flask routes
│   ├── services/           # Business logic
│   ├── repository/         # Database operations
│   ├── models/             # Database models
│   ├── tests/              # Unit tests
│   ├── database.py         # DB connection setup
│   └── error_handlers.py   # Global exception handlers
│
├── init_db.py              # Script to create tables
├── requirements.txt        # Dependencies
└── README.md
Global Exception Handling
Instead of writing try-except in every API, we have a global exception handler:

python
Copy code
# app/error_handlers.py
from flask import jsonify

def register_error_handlers(app):

    @app.errorhandler(Exception)
    def handle_exception(e):
        return jsonify({"error": str(e)}), 400
Running the Application
bash
Copy code
python -m app.main
Testing APIs in Postman
Use the following endpoints:

Method	Endpoint	Description
POST	/employees	Create a new employee
GET	/employees	Get all employees
GET	/employees/<id>	Get employee by ID
PUT	/employees/<id>	Update employee info
DELETE	/employees/<id>	Delete employee

Running Unit Tests
Unit tests are written using pytest:

bash
Copy code
python -m pytest
Understanding the Code
Controllers: Accept API requests and call service functions.
Example: employee_controller.py → create_employee() calls EmployeeService.create_employee().

Services: Contains business logic like checking if an employee already exists.

Repository: Handles database CRUD operations.
Example: EmployeeRepository.create(employee) adds an employee to the database.

Models: Define database tables.
Example: Employee table has id, name, email, department.

Global Exception Handler: Automatically catches errors and sends proper responses to the client.

Unit Tests: Verify that each part of the application works correctly using mock data.