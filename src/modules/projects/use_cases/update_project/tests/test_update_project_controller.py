from django.test import Client
from django.test import TestCase
from src.utils.test.create_project import create_project

class UpdateProjectControllerTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_update_project(self):
        project = create_project()

        project_update = {
            'name': 'Project Test 2',
        }
        
        update_response = self.client.put(f'/v1/projects/update/{project["id"]}', project_update, content_type='application/json')
        update_response_json = update_response.json()

        self.assertIn('project', update_response_json)
        self.assertEqual(update_response.status_code, 200)
        self.assertIn('id', update_response_json['project'])
        self.assertEqual('Project Test 2', update_response_json['project']['name'])

    def test_update_project_if_method_not_allowed(self):
        response = self.client.get('/v1/projects/update/1')

        self.assertEqual(response.status_code, 405)