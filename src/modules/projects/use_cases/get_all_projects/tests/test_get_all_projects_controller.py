from django.test import Client
from django.test import TestCase
from src.utils.test.create_project import create_project

class GetAllProjectsControllerTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_get_all_projects(self):
        create_project()

        project_response = self.client.get('/api/projects/get/all')

        self.assertEqual(project_response.status_code, 200)
        self.assertIn('projects', project_response.json())

    def test_get_all_projects_if_method_not_allowed(self):
        response = self.client.post('/api/projects/get/all')

        self.assertEqual(response.status_code, 405)