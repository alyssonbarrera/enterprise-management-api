from django.test import Client
from django.test import TestCase
from src.utils.test.create_project_with_employee import create_project_with_employee

class FetchProjectMetricsControllerTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_fetch_project_metrics(self):
        project = create_project_with_employee()

        response = self.client.get(f'/v1/projects/metrics/{project["id"]}')
        response_json = response.json()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response_json['metrics']['num_employees'], 1)
        self.assertEqual(response_json['metrics']['id'], str(project['id']))
        self.assertEqual(response_json['metrics']['name'], project['name'])

    def test_fetch_project_metrics_if_method_not_allowed(self):
        response = self.client.post('/v1/projects/metrics/1')

        self.assertEqual(response.status_code, 405)