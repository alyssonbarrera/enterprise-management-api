from django.test import Client
from django.test import TestCase

class GetDepartmentControllerTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_get_department(self):
        data = {
            'name': 'Department Test',
            'description': 'Department Test Description',
        }

        create_response = self.client.post('/api/departments/create', data, content_type='application/json').json()

        get_response = self.client.get('/api/departments/get/' + create_response['department']['id'])

        self.assertEqual(get_response.status_code, 200)
        self.assertIn('department', get_response.json())

    def test_get_department_if_method_not_allowed(self):
        response = self.client.delete('/api/departments/get/1')

        self.assertEqual(response.status_code, 405)