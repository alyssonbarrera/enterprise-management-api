from django.test import Client
from django.test import TestCase

class CreateDepartmentControllerTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_create_department(self):
        data = {
            'name': 'Department Test',
            'description': 'Department Test Description',
        }
        response = self.client.post('/api/departments/create', data, content_type='application/json')
        response_data = response.json()

        self.assertIn('department', response_data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response_data['department']['name'], 'Department Test')
        self.assertEqual(response_data['department']['description'], 'Department Test Description')

    def test_create_department_if_name_is_empty(self):
        data = {
            'name': '',
            'description': 'Department Test Description',
        }
        response = self.client.post('/api/departments/create', data, content_type='application/json')
        response_data = response.json()

        self.assertEqual(response.status_code, 400)
        self.assertIn('validation_error', response_data['message'])

    def test_create_department_if_methot_is_not_allowed(self):
        response = self.client.put('/api/departments/create')

        self.assertEqual(response.status_code, 405)