from django.test import TestCase
from src.shared.errors.AppError import AppError
from src.utils.error_messages import EMPLOYEE_DUPLICATE_ENTRY, EMPLOYEE_NOT_FOUND
from ....repositories.employees_repository import EmployeesRepository
from ...update_employee.update_employee_use_case import UpdateEmployeeUseCase
from src.utils.test.create_department_and_employee import create_department_and_employee

class UpdateEmployeeUseCaseTest(TestCase):
    def setUp(self):
        self.employees_repository = EmployeesRepository()
        self.use_case = UpdateEmployeeUseCase(self.employees_repository)

    def test_update_employee(self):
        data = create_department_and_employee()

        employee = data['employee']

        employee_update = {
            'name': 'Employee Test 2',
        }

        updated_employee = self.use_case.execute(employee['id'], employee_update)

        self.assertTrue(updated_employee['updated_at'] is not None)
        self.assertEqual(updated_employee['name'], "Employee Test 2")

    def test_update_employee_if_not_exists(self):
        employee_update = {
            'name': 'Employee Test 2',
        }

        with self.assertRaises(Exception) as context:
            self.use_case.execute('00000000-0000-0000-0000-000000000000', employee_update)

        self.assertIsInstance(context.exception, AppError)
        self.assertEqual(context.exception.message, EMPLOYEE_NOT_FOUND)

    def test_update_employee_with_name_already_exists(self):
        create_department_and_employee(1)
        data_2 = create_department_and_employee(2)

        employee_2 = data_2['employee']

        employee_update = {
            'name': 'Employee Test 1',
        }

        with self.assertRaises(Exception) as context:
            self.use_case.execute(employee_2['id'], employee_update)

        self.assertIsInstance(context.exception, AppError)
        self.assertEqual(context.exception.message, EMPLOYEE_DUPLICATE_ENTRY)
