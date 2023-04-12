from django.test import TestCase, Client
from src.utils.test.create_department_and_employee import create_department_and_employee

class CreateProjectControllerTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_create_project(self):
        data = create_department_and_employee()

        department = data['department']

        project_data = {
            'name': 'Project Test',
            'description': 'Project Test Description',
            'department': department['id'],
            'estimated_deadline': '20/04/2023'
        }

        project_response = self.client.post('/api/projects/create', project_data, content_type='application/json')

        self.assertEqual(project_response.status_code, 201)
        self.assertIn('project', project_response.json())

    def test_create_project_if_method_not_allowed(self):
        response = self.client.get('/api/projects/create')

        self.assertEqual(response.status_code, 405)

    def test_create_project_with_employee(self):
        data = create_department_and_employee()

        department = data['department']
        employee = data['employee']

        project_data = {
            'name': 'Project Test',
            'description': 'Project Test Description',
            'department': department['id'],
            'employees': [employee['id']],
            'estimated_deadline': '20/04/2023'
        }

        project_response = self.client.post('/api/projects/create', project_data, content_type='application/json')
        project_response_json = project_response.json()

        self.assertIn('project', project_response_json)
        self.assertEqual(project_response.status_code, 201)
        self.assertTrue(project_response_json['project']['supervisor'] is None)
        self.assertTrue(project_response_json, 'supervisor' not in project_response_json['project'])

    def test_create_project_with_supervisor(self):
        data = create_department_and_employee()

        department = data['department']
        employee = data['employee']

        project_data = {
            'name': 'Project Test',
            'description': 'Project Test Description',
            'department': department['id'],
            'supervisor': employee['id'],
            'estimated_deadline': '20/04/2023'
        }

        project_response = self.client.post('/api/projects/create', project_data, content_type='application/json')
        project_response_json = project_response.json()

        self.assertIn('project', project_response_json)
        self.assertEqual(project_response.status_code, 201)
        self.assertEqual(project_response_json['project']['employees'], [])
        self.assertTrue(project_response_json, 'supervisor' in project_response_json['project'])
