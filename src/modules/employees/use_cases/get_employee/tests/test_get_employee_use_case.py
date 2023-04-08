from django.test import TestCase
from src.shared.errors.AppError import AppError
from ...get_employee.get_employee_use_case import GetEmployeeUseCase
from ....repositories.employees_repository import EmployeesRepository
from .....departments.repositories.departments_repository import DepartmentsRepository

class GetEmployeeUseCaseTest(TestCase):
    def setUp(self):
        self.employees_repository = EmployeesRepository()
        self.departments_repository = DepartmentsRepository()
        self.use_case = GetEmployeeUseCase(self.employees_repository)

    def test_get_employee(self):
        department_data = {
            'name': 'Department Test',
            'description': 'Department Test Description',
        }

        department = self.departments_repository.create(department_data)

        employee_data = {
            'name': 'Employee Test',
            'cpf': '12345678901',
            'rg': '123456789',
            'gender': 'Male',
            'birth_date': '1990-01-01',
            'has_driving_license': True,
            'salary': 1000.00,
            'weekly_workload': 40,
            'department': department,
        }

        employee = self.employees_repository.create(employee_data)
        employee_dict = employee.to_dict()

        get_employee = self.use_case.execute(employee_dict['id'])

        self.assertEqual(get_employee['name'], 'Employee Test')

    def test_get_employee_if_not_exists(self):
        with self.assertRaises(Exception) as context:
            self.use_case.execute('00000000-0000-0000-0000-000000000000')
        self.assertIsInstance(context.exception, AppError)