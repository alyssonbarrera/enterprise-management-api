from django.test import TestCase
from src.shared.errors.AppError import AppError
from src.utils.error_messages import PROJECT_NOT_FOUND
from src.utils.test.create_project import create_project
from ..find_project_by_criteria_use_case import FindProjectByCriteriaUseCase
from ....repositories.projects_repository import ProjectsRepository

class FindProjectByCriteriaUseCaseTest(TestCase):
    def setUp(self):
        self.projects_repository = ProjectsRepository()
        self.use_case = FindProjectByCriteriaUseCase(self.projects_repository)

    def test_find_project_by_criteria(self):
        project = create_project()

        criteria = {
            'id': project['id']
        }

        get_project = self.use_case.execute(criteria)

        self.assertEqual(get_project['name'], 'Project Test 1')
        self.assertEqual(get_project['id'], project['id'])

    def test_find_project_by_criteria_returns_none_if_criteria_do_not_match_any_project(self):
        with self.assertRaises(Exception) as context:
            self.use_case.execute({'id': 1})
        self.assertIsInstance(context.exception, AppError)
        self.assertEqual(context.exception.message, PROJECT_NOT_FOUND)