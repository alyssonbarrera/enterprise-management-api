from django.test import Client
from django.test import TestCase

class GetAllDepartmentsControllerTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_get_all_departments(self):
        data = {
            'name': 'Department Test',
            'description': 'Department Test Description',
        }
        
        self.client.post('/v1/departments/create', data, content_type='application/json')

        get_all_response = self.client.get('/v1/departments/get/all')

        self.assertEqual(get_all_response.status_code, 200)
        self.assertIn('departments', get_all_response.json())
        self.assertEqual(len(get_all_response.json()['departments']), 1)

    def test_get_all_departments_if_method_not_allowed(self):
        response = self.client.post('/v1/departments/get/all')

        self.assertEqual(response.status_code, 405)