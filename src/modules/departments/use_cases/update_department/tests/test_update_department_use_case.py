from django.test import TestCase
from src.shared.errors.AppError import AppError
from ....repositories.departments_repository import DepartmentsRepository
from ...update_department.update_department_use_case import UpdateDepartmentUseCase

class UpdateDepartmentUseCaseTest(TestCase):
    def setUp(self):
        self.departments_repository = DepartmentsRepository()
        self.use_case = UpdateDepartmentUseCase(self.departments_repository)

    def test_update_department(self):
        data = {
            'name': 'Department Test 1',
            'description': 'Department Test Description 1',
        }
        data_update = {
            'name': 'Department Test 2',
            'description': 'Department Test Description 2',
        }
        create_department = self.departments_repository.create(data).to_dict()

        updated_department = self.use_case.execute(create_department['id'], data_update)

        self.assertTrue(updated_department['updated_at'] is not None)
        self.assertEqual(updated_department['name'], "Department Test 2")

    def test_update_department_if_not_exists(self):
        data = {
            'name': 'Department Test 1',
            'description': 'Department Test Description 1',
        }

        with self.assertRaises(Exception) as context:
            self.use_case.execute('00000000-0000-0000-0000-000000000000', data)

        self.assertIsInstance(context.exception, AppError)

    def test_update_department_with_name_already_exists(self):
        data_one = {
            'name': 'Department Test 1',
            'description': 'Department Test Description 1',
        }

        data_two = {
            'name': 'Department Test 2',
            'description': 'Department Test Description 2',
        }

        data_update = {
            'name': 'Department Test 1',
            'description': 'Department Test Description 1',
        }

        self.departments_repository.create(data_one)

        create_department_two = self.departments_repository.create(data_two).to_dict()
        
        with self.assertRaises(Exception) as context:
            self.use_case.execute(create_department_two['id'], data_update)

        self.assertIsInstance(context.exception, AppError)