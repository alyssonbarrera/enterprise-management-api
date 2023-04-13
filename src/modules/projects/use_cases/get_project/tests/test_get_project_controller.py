from django.test import Client
from django.test import TestCase
from src.utils.test.create_project import create_project

class GetProjectControllerTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_get_project(self):
        project = create_project()

        get_response = self.client.get(f'/api/projects/get/{project["id"]}')

        self.assertEqual(get_response.status_code, 200)
        self.assertIn('project', get_response.json())

    def test_get_project_if_invalid_id(self):
        response = self.client.get('/api/projects/get/id')
        response_json = response.json()

        self.assertEqual(response.status_code, 400)
        self.assertIn('validation_error', response_json['message'])

    def test_get_project_if_method_not_allowed(self):
        response = self.client.put('/api/projects/get/id')

        self.assertEqual(response.status_code, 405)