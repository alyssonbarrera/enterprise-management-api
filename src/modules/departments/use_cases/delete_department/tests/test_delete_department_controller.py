from django.test import Client
from django.test import TestCase

class DeleteDepartmentControllerTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_delete_department(self):
        data = {
            'name': 'Department Test',
            'description': 'Department Test Description',
        }
        
        create_response = self.client.post('/api/departments/create', data, content_type='application/json').json()

        delete_response = self.client.delete(f'/api/departments/delete/' + create_response['department']['id'])

        self.assertEqual(delete_response.status_code, 204)

    def test_delete_department_if_method_not_allowed(self):
        response = self.client.get('/api/departments/delete/1')

        self.assertEqual(response.status_code, 405)