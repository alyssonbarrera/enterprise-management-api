from django.test import Client
from django.test import TestCase
from src.utils.test.create_department_and_employee import create_department_and_employee

class UpdateEmployeeControllerTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_update_employee(self):
        data = create_department_and_employee()

        employee = data['employee']

        employee_update = {
            'name': 'Employee Test 2',
        }
        
        update_response = self.client.put(f'/v1/employees/update/{employee["id"]}', employee_update, content_type='application/json')
        update_response_json = update_response.json()

        self.assertIn('employee', update_response_json)
        self.assertEqual(update_response.status_code, 200)
        self.assertIn('id', update_response_json['employee'])
        self.assertEqual('Employee Test 2', update_response_json['employee']['name'])

    def test_update_employee_if_method_not_allowed(self):
        response = self.client.get('/v1/employees/update/1')

        self.assertEqual(response.status_code, 405)