from django.test import Client
from django.test import TestCase
from src.utils.test.create_department_and_employee import create_department_and_employee

class FindEmployeeByCriteriaControllerTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_find_employee_by_criteria(self):
        data = create_department_and_employee()

        employee = data['employee']

        query = {
            'id': employee['id'],
            'name': employee['name'],
            'cpf': employee['cpf'],
            'rg': employee['rg'],
        }

        get_response = self.client.get(f'/v1/employees/get', query)

        self.assertEqual(get_response.status_code, 200)
        self.assertIn('employee', get_response.json())

    def test_find_employee_by_criteria_if_not_found(self):
        response = self.client.get('/v1/employees/get')
        response_json = response.json()

        self.assertEqual(response.status_code, 400)
        self.assertIn('validation_error', response_json['message'])

    def test_find_employee_by_criteria_if_method_not_allowed(self):
        response = self.client.put('/v1/employees/get')

        self.assertEqual(response.status_code, 405)