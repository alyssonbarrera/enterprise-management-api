from django.test import TestCase
from src.shared.errors.AppError import AppError
from src.utils.error_messages import PROJECT_NOT_FOUND
from src.utils.test.create_project import create_project
from src.utils.test.create_project_with_employee import create_project_with_employee
from src.modules.projects.repositories.projects_repository import ProjectsRepository
from src.modules.projects.use_cases.delete_project.delete_project_use_case import DeleteProjectUseCase
from src.modules.projects.repositories.projects_employees_repository import ProjectsEmployeesRepository

class DeleteProjectUseCaseTest(TestCase):
    def setUp(self):
        self.projects_repository = ProjectsRepository()
        self.projects_employees_repository = ProjectsEmployeesRepository()
        self.use_case = DeleteProjectUseCase(self.projects_repository)

    def test_delete_project(self):
        project = create_project()

        self.use_case.execute(project['id'])

        get_project = self.projects_repository.get(project['id'])

        self.assertIsNone(get_project)

    def test_delete_project_if_not_exists(self):
        with self.assertRaises(Exception) as context:
            self.use_case.execute('00000000-0000-0000-0000-000000000000')
        self.assertIsInstance(context.exception, AppError)
        self.assertEqual(context.exception.message, PROJECT_NOT_FOUND)

    def test_delete_project_with_employee(self):
        project = create_project_with_employee()

        self.use_case.execute(project['id'])

        get_project = self.projects_repository.get(project['id'])
        get_project_employees = self.projects_employees_repository.get_by_project(project['id'])

        self.assertIsNone(get_project)
        self.assertEqual(len(get_project_employees), 0)