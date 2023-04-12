from django.test import Client
from django.test import TestCase

class UpdateDepartmentControllerTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_update_department(self):
        data = {
            'name': 'Department Test',
            'description': 'Department Test Description',
        }

        data_update = {
            'name': 'Department Test Update',
            'description': 'Department Test Description Update',
        }

        create_response = self.client.post('/api/departments/create', data, content_type='application/json').json()

        update_response = self.client.put('/api/departments/update/' + create_response['department']['id'], data_update, content_type='application/json')

        self.assertEqual(update_response.status_code, 200)
        self.assertIn('department', update_response.json())
        self.assertDictContainsSubset(data_update, update_response.json()['department'])

    def test_update_department_if_method_not_allowed(self):
        response = self.client.get('/api/departments/update/1')

        self.assertEqual(response.status_code, 405)