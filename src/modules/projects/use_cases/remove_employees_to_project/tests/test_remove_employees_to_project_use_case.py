from django.test import TestCase
from src.shared.errors.AppError import AppError
from src.utils.error_messages import PROJECT_NOT_FOUND
from ....repositories.projects_repository import ProjectsRepository
from .....employees.repositories.employees_repository import EmployeesRepository
from ..remove_employees_to_project_use_case import RemoveEmployeesToProjectUseCase
from src.utils.test.create_project_with_employee import create_project_with_employee
from ....repositories.projects_employees_repository import ProjectsEmployeesRepository

class RemoveEmployeesToProjectUseCaseTest(TestCase):
    def setUp(self):
        self.projects_repository = ProjectsRepository()
        self.employees_repository = EmployeesRepository()
        self.projects_employees_repository = ProjectsEmployeesRepository()
        self.remove_employees_to_project_use_case = RemoveEmployeesToProjectUseCase(
            self.projects_repository,
            self.employees_repository,
            self.projects_employees_repository
        )

    def test_remove_employees_to_project(self):
        project = create_project_with_employee()

        employee = project['employees'][0]

        employee_ids = [employee['id']]

        project = self.remove_employees_to_project_use_case.execute(project['id'], employee_ids)

        self.assertEqual(project['name'], project['name'])
        self.assertEqual(len(project['employees']), 0)

    def test_remove_employees_to_project_with_invalid_project_id(self):
        project = create_project_with_employee()

        employee = project['employees'][0]

        employee_ids = [employee['id']]

        with self.assertRaises(AppError) as context:
            self.remove_employees_to_project_use_case.execute('00000000-0000-0000-0000-000000000000', employee_ids)

        self.assertIsInstance(context.exception, AppError)
        self.assertEqual(context.exception.message, PROJECT_NOT_FOUND)

    def test_remove_employees_to_project_with_invalid_employee_id(self):
        project = create_project_with_employee()

        with self.assertRaises(AppError) as context:
            self.remove_employees_to_project_use_case.execute(project['id'], ['00000000-0000-0000-0000-000000000000'])

        self.assertIsInstance(context.exception, AppError)
        self.assertEqual(context.exception.message, 'Employee with id 00000000-0000-0000-0000-000000000000 not found')