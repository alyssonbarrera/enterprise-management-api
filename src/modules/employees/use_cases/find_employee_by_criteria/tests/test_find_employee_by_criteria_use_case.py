from django.test import TestCase
from src.shared.errors.AppError import AppError
from src.utils.error_messages import EMPLOYEE_NOT_FOUND
from ..find_employee_by_criteria_use_case import FindEmployeeByCriteriaUseCase
from ....repositories.employees_repository import EmployeesRepository
from .....departments.repositories.departments_repository import DepartmentsRepository
from src.utils.test.create_department_and_employee import create_department_and_employee

class FindEmployeeByCriteriaUseCaseTest(TestCase):
    def setUp(self):
        self.employees_repository = EmployeesRepository()
        self.departments_repository = DepartmentsRepository()
        self.use_case = FindEmployeeByCriteriaUseCase(self.employees_repository)

    def test_find_employee_by_criteria(self):
        data = create_department_and_employee()

        employee = data['employee']

        criteria = {
            'id': employee['id']
        }

        get_employee = self.use_case.execute(criteria)

        self.assertEqual(get_employee['name'], 'Employee Test 1')
        self.assertEqual(get_employee['id'], employee['id'])

    def test_find_employee_by_criteria_returns_none_if_criteria_do_not_match_any_employee(self):
        with self.assertRaises(Exception) as context:
            self.use_case.execute({'id': 1})
        self.assertIsInstance(context.exception, AppError)
        self.assertEqual(context.exception.message, EMPLOYEE_NOT_FOUND)