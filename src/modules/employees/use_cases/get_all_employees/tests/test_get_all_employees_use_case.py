from django.test import TestCase
from ....repositories.employees_repository import EmployeesRepository
from ...get_all_employees.get_all_employees_use_case import GetAllEmployeesUseCase
from src.utils.test.create_department_and_employee import create_department_and_employee

class GetAllEmployeesUseCaseTest(TestCase):
    def setUp(self):
        self.employees_repository = EmployeesRepository()
        self.use_case = GetAllEmployeesUseCase(self.employees_repository)

    def test_get_all_employees(self):
        create_department_and_employee()

        employees = self.use_case.execute(1)

        self.assertEqual(len(employees), 2)
        self.assertTrue(employees[0]['id'] is not None)

    def test_get_all_employees_if_not_exists(self):
        employees = self.use_case.execute(1)
        self.assertEqual(len(employees), 0)

    def test_get_all_employees_if_page_is_two(self):
        employee_number = 0
        while employee_number < 25:
            create_department_and_employee(employee_number)
            employee_number += 1

        employees = self.use_case.execute(2)

        self.assertNotEqual(list(employees), [])