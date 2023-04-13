from django.test import TestCase
from src.shared.errors.AppError import AppError
from src.utils.error_messages import PROJECT_NOT_FOUND
from ..get_project_use_case import GetProjectUseCase
from src.utils.test.create_project import create_project
from ....repositories.projects_repository import ProjectsRepository

class GetProjectUseCaseTest(TestCase):
    def setUp(self):
        self.projects_repository = ProjectsRepository()
        self.use_case = GetProjectUseCase(self.projects_repository)

    def test_get_project(self):
        project = create_project()

        get_project = self.use_case.execute(project['id'])

        self.assertEqual(get_project['name'], 'Project Test 1')
        self.assertEqual(get_project['id'], project['id'])

    def test_get_project_not_exists(self):
        with self.assertRaises(Exception) as context:
            self.use_case.execute('00000000-0000-0000-0000-000000000000')
        self.assertIsInstance(context.exception, AppError)
        self.assertEqual(context.exception.message, PROJECT_NOT_FOUND)