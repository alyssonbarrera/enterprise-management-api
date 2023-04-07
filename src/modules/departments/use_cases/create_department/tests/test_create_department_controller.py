from django.test import Client
from django.test import TestCase

class MyTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_create_department(self):
        data = {
            'name': 'Department 1'
        }
        response = self.client.post('/v1/departments/create', data, content_type='application/json')
        response_data = response.json()

        self.assertEqual(response.status_code, 201)
        self.assertIn('department', response_data)
        self.assertEqual(response_data['department']['name'], 'Department 1')