from django.test import Client
from django.test import TestCase
from src.utils.test.create_project import create_project

class SearchProjectsControllerTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_search_projects(self):
        project = create_project()

        get_response = self.client.get('/api/projects/search?query=' + project['name'])

        self.assertEqual(get_response.status_code, 200)
        self.assertIn('projects', get_response.json())

    def test_search_projects_if_method_not_allowed(self):
        response = self.client.post('/api/projects/search?query=1')

        self.assertEqual(response.status_code, 405)