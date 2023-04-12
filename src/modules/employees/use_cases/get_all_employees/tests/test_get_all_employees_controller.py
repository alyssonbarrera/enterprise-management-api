from django.test import Client
from django.test import TestCase
from src.utils.test.create_department_and_employee import create_department_and_employee

class GetAllEmployeesControllerTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_get_all_employees(self):
        create_department_and_employee()

        employee_response = self.client.get('/api/employees/get/all')

        self.assertEqual(employee_response.status_code, 200)
        self.assertIn('employees', employee_response.json())

    def test_get_all_employees_if_method_not_allowed(self):
        response = self.client.post('/api/employees/get/all')

        self.assertEqual(response.status_code, 405)