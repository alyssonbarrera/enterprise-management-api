from django.test import Client
from django.test import TestCase
from src.utils.test.create_project import create_project
from src.utils.test.create_department_and_employee import create_department_and_employee

class RemoveEmployeesToProjectControllerTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_remove_employees_to_project(self):
        data = create_department_and_employee(30)
        project = create_project()

        employee = data['employee']

        employees_ids = [employee['id']]

        remove_employees_to_project_response = self.client.patch(f'/api/projects/remove/employees/{project["id"]}', {'employees': employees_ids}, content_type='application/json')
        remove_employees_to_project_response_json = remove_employees_to_project_response.json()

        self.assertIn('project', remove_employees_to_project_response_json)
        self.assertEqual(remove_employees_to_project_response.status_code, 200)
        self.assertIn('id', remove_employees_to_project_response_json['project'])

    def test_remove_employees_to_project_if_method_not_allowed(self):
        response = self.client.get('/api/projects/add/employees/1')

        self.assertEqual(response.status_code, 405)