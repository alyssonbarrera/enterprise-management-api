from django.test import TestCase
from ....repositories.departments_repository import DepartmentsRepository
from ..search_departments_use_case import SearchDepartmentsUseCase

class SearchDepartmentsUseCaseTest(TestCase):
    def setUp(self):
        self.departments_repository = DepartmentsRepository()
        self.use_case = SearchDepartmentsUseCase(self.departments_repository)

    def test_search_departments(self):
        data = {
            'name': 'Department Test',
            'description': 'Department Test Description',
        }
        
        create_department = self.departments_repository.create(data).to_dict()
       
        department = self.use_case.execute(create_department['name'])

        self.assertListEqual(department, [create_department])
        self.assertEqual(department[0]['id'], create_department['id'])

    def test_search_departments_if_not_exists(self):
        department = self.use_case.execute('Department 1')
        self.assertListEqual(department, [])