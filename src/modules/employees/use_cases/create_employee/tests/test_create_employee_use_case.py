from uuid import UUID
from django.test import TestCase
from src.shared.errors.AppError import AppError
from src.modules.employees.repositories.employees_repository import EmployeesRepository
from src.modules.departments.repositories.departments_repository import DepartmentsRepository
from src.modules.employees.use_cases.create_employee.create_employee_use_case import CreateEmployeeUseCase

class CreateEmployeeUseCaseTest(TestCase):
    def setUp(self):
        self.employees_repository = EmployeesRepository()
        self.departments_repository = DepartmentsRepository()
        self.use_case = CreateEmployeeUseCase(
            self.employees_repository,
            self.departments_repository
        )

    def test_create_employee(self):
        department_data = {
            'name': 'Department Test',
            'description': 'Department Test Description',
        }

        department = self.departments_repository.create(department_data)
        department_dict = department.to_dict()

        employee_data = {
            'name': 'Employee Test',
            'cpf': '12345678901',
            'rg': '123456789',
            'gender': 'Male',
            'birth_date': '1990-01-01',
            'has_driving_license': True,
            'salary': 1000.00,
            'weekly_workload': 40,
            'department': department_dict['id'],
        }

        employee = self.use_case.execute(employee_data)
        
        self.assertTrue(employee['active'] is True)
        self.assertTrue(employee['updated_at'] is None)
        self.assertTrue(isinstance(employee['id'], UUID))
        self.assertTrue(employee['created_at'] is not None)
        self.assertEqual(employee['name'], "Employee Test")

    def test_create_employee_with_invalid_department(self):
        employee_data = {
            'name': 'Employee Test',
            'cpf': '12345678901',
            'rg': '123456789',
            'gender': 'Male',
            'birth_date': '1990-01-01',
            'has_driving_license': True,
            'salary': 1000.00,
            'weekly_workload': 40,
            'department': '00000000-0000-0000-0000-000000000000',
        }

        with self.assertRaises(Exception) as context:
            self.use_case.execute(employee_data)
        self.assertIsInstance(context.exception, AppError)
        self.assertEqual(context.exception.message, 'Department not found')

    def test_create_employee_duplicate(self):
        department_data = {
            'name': 'Department Test',
            'description': 'Department Test Description',
        }
 
        department = self.departments_repository.create(department_data)
        department_dict = department.to_dict()

        employee_data_1 = {
            'name': 'Employee Test',
            'cpf': '12345678901',
            'rg': '123456789',
            'gender': 'Male',
            'birth_date': '1990-01-01',
            'has_driving_license': True,
            'salary': 1000.00,
            'weekly_workload': 40,
            'department': department_dict['id'],
        }

        employee_data_2 = {
            'name': 'Employee Test',
            'cpf': '12345678901',
            'rg': '123456789',
            'gender': 'Male',
            'birth_date': '1990-01-01',
            'has_driving_license': True,
            'salary': 1000.00,
            'weekly_workload': 40,
            'department': department_dict['id'],
        }

        self.use_case.execute(employee_data_1)

        with self.assertRaises(Exception) as context:
            self.use_case.execute(employee_data_2)
        self.assertIsInstance(context.exception, AppError)
        self.assertEqual(context.exception.message, 'Employee already exists')