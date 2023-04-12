from django.test import Client
from django.test import TestCase
from src.utils.test.create_project_with_employee import create_project_with_employee

class DeleteProjectControllerTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_delete_project(self):
        project = create_project_with_employee()

        delete_response = self.client.delete(f'/api/projects/delete/{project["id"]}')

        self.assertEqual(delete_response.status_code, 204)

    def test_delete_project_if_method_not_allowed(self):
        response = self.client.get('/api/projects/delete/1')

        self.assertEqual(response.status_code, 405)