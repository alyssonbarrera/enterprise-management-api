from django.test import Client
from django.test import TestCase

class SearchDepartmentsControllerTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_search_departments(self):
        data = {
            'name': 'Department Test',
            'description': 'Department Test Description',
        }

        create_response = self.client.post('/v1/departments/create', data, content_type='application/json').json()

        get_response = self.client.get('/v1/departments/search?query=' + create_response['department']['name'])

        self.assertEqual(get_response.status_code, 200)
        self.assertIn('departments', get_response.json())

    def test_search_departments_if_method_not_allowed(self):
        response = self.client.post('/v1/departments/search?query=1')

        self.assertEqual(response.status_code, 405)