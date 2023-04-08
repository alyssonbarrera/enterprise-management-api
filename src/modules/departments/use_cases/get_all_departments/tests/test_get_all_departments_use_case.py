from django.test import TestCase
from ....repositories.departments_repository import DepartmentsRepository
from ...get_all_departments.get_all_departments_use_case import GetAllDepartmentsUseCase

class GetAllDepartmentsUseCaseTest(TestCase):
    def setUp(self):
        self.departments_repository = DepartmentsRepository()
        self.use_case = GetAllDepartmentsUseCase(self.departments_repository)

    def test_get_all_departments(self):
        data = {
            'name': 'Department Test 1',
            'description': 'Department Test Description 1',
        }
        
        self.departments_repository.create(data)
        
        data = {
            'name': 'Department Test 2',
            'description': 'Department Test Description 2',
        }

        self.departments_repository.create(data)

        departments = self.use_case.execute(1)

        self.assertEqual(len(departments), 2)
        self.assertTrue(departments[0]['id'] is not None)
        self.assertTrue(departments[1]['id'] is not None)

    def test_get_all_departments_if_not_exists(self):
        departments = self.use_case.execute(1)
        self.assertEqual(len(departments), 0)