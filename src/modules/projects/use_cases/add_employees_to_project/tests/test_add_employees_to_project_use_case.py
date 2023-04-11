from django.test import TestCase
from src.shared.errors.AppError import AppError
from src.utils.error_messages import PROJECT_NOT_FOUND
from src.utils.test.create_project import create_project
from ....repositories.projects_repository import ProjectsRepository
from .....employees.repositories.employees_repository import EmployeesRepository
from ....repositories.projects_employees_repository import ProjectsEmployeesRepository
from src.utils.test.create_department_and_employee import create_department_and_employee
from ...add_employees_to_project.add_employees_to_project_use_case import AddEmployeesToProjectUseCase

class AddEmployeesToProjectUseCaseTest(TestCase):
    def setUp(self):
        self.projects_repository = ProjectsRepository()
        self.employees_repository = EmployeesRepository()
        self.projects_employees_repository = ProjectsEmployeesRepository()
        self.add_employees_to_project_use_case = AddEmployeesToProjectUseCase(
            self.projects_repository,
            self.employees_repository,
            self.projects_employees_repository
        )

    def test_add_employees_to_project(self):
        data_1 = create_department_and_employee(10)
        data_2 = create_department_and_employee(20)

        project = create_project()

        employee_1 = data_1['employee']
        employee_2 = data_2['employee']

        employee_ids = [employee_1['id'], employee_2['id']]

        project = self.add_employees_to_project_use_case.execute(project['id'], employee_ids)

        self.assertEqual(project['name'], project['name'])
        self.assertEqual(project['employees'][0]['name'], employee_1['name'])
        self.assertEqual(project['employees'][1]['name'], employee_2['name'])

    def test_add_employees_to_project_with_invalid_project_id(self):
        data_1 = create_department_and_employee(10)
        data_2 = create_department_and_employee(20)

        employee_1 = data_1['employee']
        employee_2 = data_2['employee']

        employee_ids = [employee_1['id'], employee_2['id']]

        with self.assertRaises(AppError) as context:
            self.add_employees_to_project_use_case.execute('00000000-0000-0000-0000-000000000000', employee_ids)

        self.assertIsInstance(context.exception, AppError)
        self.assertEqual(context.exception.message, PROJECT_NOT_FOUND)

    def test_add_employee_to_project_with_invalid_employee_id(self):
        project = create_project()

        employee_id = ['00000000-0000-0000-0000-000000000000']

        with self.assertRaises(Exception) as context:
            self.add_employees_to_project_use_case.execute(project['id'], employee_id)

        self.assertIsInstance(context.exception, AppError)

    def test_add_employee_has_no_hours(self):
        data = create_department_and_employee(10)

        project = create_project()

        employee = data['employee']

        employee_ids = [employee['id'], employee['id']]

        with self.assertRaises(Exception) as context:
            self.add_employees_to_project_use_case.execute(project['id'], employee_ids)

        self.assertIsInstance(context.exception, AppError)