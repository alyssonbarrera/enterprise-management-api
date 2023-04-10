from src.modules.departments.repositories.departments_repository import DepartmentsRepository
from src.modules.employees.repositories.employees_repository import EmployeesRepository

def create_department_and_employee(number=1):
    departments_repository = DepartmentsRepository()
    employees_repository = EmployeesRepository()

    department_data = {
        'name': f'Department Test {number}',
        'description': 'Department Test Description',
    }

    department = departments_repository.create(department_data)
    department_dict = department.to_dict()

    employee_data = {
        'name': f'Employee Test {number}',
        'cpf': f'1234567890{number}',
        'rg': f'12345678{number}',
        'gender': 'Male',
        'birth_date': '01/01/2001',
        'has_driving_license': True,
        'salary': 1000.00,
        'weekly_workload': 40,
        'department': department,
    }

    employee = employees_repository.create(employee_data)
    employee_dict = employee.to_dict()

    return {
        'department': department_dict,
        'employee': employee_dict,
    }