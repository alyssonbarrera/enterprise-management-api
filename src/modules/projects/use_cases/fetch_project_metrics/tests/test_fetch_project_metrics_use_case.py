from django.test import TestCase
from src.shared.errors.AppError import AppError
from src.utils.error_messages import PROJECT_NOT_FOUND
from src.utils.test.create_project import create_project
from ....repositories.projects_repository import ProjectsRepository
from ..fetch_project_metrics_use_case import FetchProjectMetricsUseCase
from src.utils.test.create_project_with_employee import create_project_with_employee

class FetchProjectMetricsUseCaseTest(TestCase):
    def setUp(self):
        self.projects_repository = ProjectsRepository()
        self.use_case = FetchProjectMetricsUseCase(self.projects_repository)

    def test_fetch_project_metrics(self):
        project = create_project()

        project_metrics = self.use_case.execute(project['id'])

        self.assertEqual(project_metrics['num_employees'], 0)
        self.assertEqual(project_metrics['id'], project['id'])
        self.assertTrue(project_metrics['remaining_hours'] >= 0)
        self.assertEqual(project_metrics['name'], project['name'])

    def test_fetch_project_metrics_if_not_exists(self):
        with self.assertRaises(Exception) as context:
            self.use_case.execute('00000000-0000-0000-0000-000000000000')
        self.assertIsInstance(context.exception, AppError)
        self.assertEqual(context.exception.message, PROJECT_NOT_FOUND)

    def test_fetch_project_metrics_with_employee(self):
        project = create_project_with_employee()

        project_metrics = self.use_case.execute(project['id'])

        self.assertEqual(project_metrics['num_employees'], 1)
        self.assertEqual(project_metrics['id'], project['id'])
        self.assertTrue(project_metrics['remaining_hours'] >= 0)
        self.assertEqual(project_metrics['name'], project['name'])