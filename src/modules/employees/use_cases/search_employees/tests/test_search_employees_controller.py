from django.test import Client
from django.test import TestCase
from src.utils.test.create_department_and_employee import create_department_and_employee

class SearchEmployeesControllerTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_search_employees(self):
        data = create_department_and_employee()

        employee = data['employee']

        get_response = self.client.get('/v1/employees/search?query=' + employee['name'])

        self.assertEqual(get_response.status_code, 200)
        self.assertIn('employees', get_response.json())

    def test_search_employees_if_method_not_allowed(self):
        response = self.client.post('/v1/employees/search?query=1')

        self.assertEqual(response.status_code, 405)