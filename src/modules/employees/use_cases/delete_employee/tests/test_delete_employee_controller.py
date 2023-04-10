from django.test import Client
from django.test import TestCase
from src.utils.test.create_department_and_employee import create_department_and_employee

class DeleteEmployeeControllerTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_delete_employee(self):
        data = create_department_and_employee()

        employee = data['employee']

        delete_response = self.client.delete(f'/v1/employees/delete/{employee["id"]}')

        self.assertEqual(delete_response.status_code, 204)

    def test_delete_department_if_method_not_allowed(self):
        response = self.client.get('/v1/employees/delete/1')

        self.assertEqual(response.status_code, 405)