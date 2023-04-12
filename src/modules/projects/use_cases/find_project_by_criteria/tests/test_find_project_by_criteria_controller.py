from django.test import Client
from django.test import TestCase
from src.utils.test.create_project import create_project

class FindProjectByCriteriaControllerTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_find_project_by_criteria(self):
        project = create_project()

        query = {
            'id': project['id'],
            'name': project['name'],
        }

        get_response = self.client.get(f'/api/projects/get', query)

        self.assertEqual(get_response.status_code, 200)
        self.assertIn('project', get_response.json())

    def test_find_project_by_criteria_if_not_query(self):
        response = self.client.get('/api/projects/get')
        response_json = response.json()

        self.assertEqual(response.status_code, 400)
        self.assertIn('validation_error', response_json['message'])

    def test_find_project_by_criteria_if_method_not_allowed(self):
        response = self.client.put('/api/projects/get')

        self.assertEqual(response.status_code, 405)