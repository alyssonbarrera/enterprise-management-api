from django.test import TestCase
from src.shared.errors.AppError import AppError
from src.utils.error_messages import EMPLOYEE_NOT_FOUND
from src.modules.employees.repositories.employees_repository import EmployeesRepository
from src.utils.test.create_department_and_employee import create_department_and_employee
from src.modules.employees.use_cases.delete_employee.delete_employee_use_case import DeleteEmployeeUseCase

class DeleteEmployeeUseCaseTest(TestCase):
    def setUp(self):
        self.employees_repository = EmployeesRepository()
        self.use_case = DeleteEmployeeUseCase(self.employees_repository)

    def test_delete_employee(self):
        data = create_department_and_employee()

        employee = data['employee']

        self.use_case.execute(employee['id'])

        get_employee = self.employees_repository.get(employee['id'])

        self.assertIsNone(get_employee)

    def test_delete_employee_if_not_exists(self):
        with self.assertRaises(Exception) as context:
            self.use_case.execute('00000000-0000-0000-0000-000000000000')
        self.assertIsInstance(context.exception, AppError)
        self.assertEqual(context.exception.message, EMPLOYEE_NOT_FOUND)