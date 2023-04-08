from django.test import Client
from django.test import TestCase

class GetEmployeeControllerTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_get_employee(self):
        data = {
            'name': 'Department Test',
            'description': 'Department Test Description',
        }

        create_department_response = self.client.post('/v1/departments/create', data, content_type='application/json').json()

        employee_data = {
            'name': 'Employee Test',
            'cpf': '12345678901',
            'rg': '123456789',
            'gender': 'Male',
            'birth_date': '1990-01-01',
            'has_driving_license': True,
            'salary': 1000.00,
            'weekly_workload': 40,
            'department': create_department_response['department']['id'],
        }

        create_employee_response = self.client.post('/v1/employees/create', employee_data, content_type='application/json').json()

        print('ID: ', create_employee_response['employee']['id'])

        get_response = self.client.get(f'/v1/employees/get/{create_employee_response["employee"]["id"]}')

        self.assertEqual(get_response.status_code, 200)
        self.assertIn('employee', get_response.json())

    def test_get_employee_if_method_not_allowed(self):
        response = self.client.put('/v1/employees/get/id')

        self.assertEqual(response.status_code, 405)