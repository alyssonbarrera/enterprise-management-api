from django.test import TestCase
from src.utils.test.create_project import create_project
from ....repositories.projects_repository import ProjectsRepository
from ...search_projects.search_projects_use_case import SearchProjectsUseCase

class SearchProjectsUseCaseTest(TestCase):
    def setUp(self):
        self.projects_repository = ProjectsRepository()
        self.use_case = SearchProjectsUseCase(self.projects_repository)

    def test_search_projects(self):
        project = create_project()

        projects = self.use_case.execute(project['name'], 1)

        self.assertEqual(projects[0]['id'], project['id'])
        self.assertEqual(projects[0]['name'], project['name'])

    def test_search_projects_if_not_exists(self):
        projects = self.use_case.execute('Project 1', 1)
        self.assertListEqual(projects, [])