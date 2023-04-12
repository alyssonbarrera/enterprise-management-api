from django.test import Client
from django.test import TestCase

class CreateEmployeeControllerTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_create_employee(self):
        department_data = {
            'name': 'Department Test',
            'description': 'Department Test Description',
        }

        department_response = self.client.post('/api/departments/create', department_data, content_type='application/json').json()

        employee_data = {
            'name': 'Employee Test',
            'cpf': '12345678901',
            'rg': '123456789',
            'gender': 'Male',
            'birth_date': '01/01/2001',
            'has_driving_license': True,
            'salary': 1000.00,
            'weekly_workload': 40,
            'department': department_response['department']['id'],
        }

        employee_response = self.client.post('/api/employees/create', employee_data, content_type='application/json')

        self.assertEqual(employee_response.status_code, 201)
        self.assertIn('employee', employee_response.json())

    def test_create_employee_if_method_not_allowed(self):
        response = self.client.get('/api/employees/create')

        self.assertEqual(response.status_code, 405)