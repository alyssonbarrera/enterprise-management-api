from django.test import TestCase
from ....repositories.employees_repository import EmployeesRepository
from ...search_employees.search_employees_use_case import SearchEmployeesUseCase
from src.utils.test.create_department_and_employee import create_department_and_employee

class SearchEmployeesUseCaseTest(TestCase):
    def setUp(self):
        self.employees_repository = EmployeesRepository()
        self.use_case = SearchEmployeesUseCase(self.employees_repository)

    def test_search_employees(self):
        data = create_department_and_employee()

        employee = data['employee']
       
        employees = self.use_case.execute(employee['name'], 1)

        self.assertListEqual(employees, [employee])
        self.assertEqual(employees[0]['id'], employee['id'])

    def test_search_employees_if_not_exists(self):
        employees = self.use_case.execute('Employee 1', 1)
        self.assertListEqual(employees, [])