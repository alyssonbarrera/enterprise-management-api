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

    employee_data_1 = {
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

    employee_data_2 = {
        'name': f'Employee Test 1 {number}',
        'cpf': f'1234567891{number}',
        'rg': f'12345671{number}',
        'gender': 'Male',
        'birth_date': '01/01/2001',
        'has_driving_license': True,
        'salary': 1000.00,
        'weekly_workload': 0,
        'department': department,
    }

    employee_1 = employees_repository.create(employee_data_1)
    employee_2 = employees_repository.create(employee_data_2)
    employee_dict_1 = employee_1.to_dict()
    employee_dict_2 = employee_2.to_dict()

    return {
        'department': department_dict,
        'employee': employee_dict_1,
        'Department': department,
        'Employee': employee_1,
        'Employee_2': employee_2,
        'employee_2': employee_dict_2,
    }