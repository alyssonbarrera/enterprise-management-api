from django.test import TestCase
from src.utils.test.create_project import create_project
from ....repositories.projects_repository import ProjectsRepository
from ...get_all_projects.get_all_projects_use_case import GetAllProjectsUseCase

class GetAllProjectsUseCaseTest(TestCase):
    def setUp(self):
        self.projects_repository = ProjectsRepository()
        self.use_case = GetAllProjectsUseCase(self.projects_repository)

    def test_get_all_projects(self):
        create_project()

        projects = self.use_case.execute(1)

        self.assertEqual(len(projects), 1)
        self.assertTrue(projects[0]['id'] is not None)

    def test_get_all_projects_if_not_exists(self):
        projects = self.use_case.execute(1)
        self.assertEqual(len(projects), 0)

    def test_get_all_projects_if_page_is_two(self):
        project_number = 0
        while project_number < 25:
            create_project(project_number)
            project_number += 1

        projects = self.use_case.execute(2)

        self.assertEqual(projects[0]['name'], 'Project Test 20')