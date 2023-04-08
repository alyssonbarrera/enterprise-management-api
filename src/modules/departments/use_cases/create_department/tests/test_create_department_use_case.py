from uuid import UUID
from django.test import TestCase
from src.shared.errors.AppError import AppError
from ...create_department.create_department_use_case import CreateDepartmentUseCase
from ....repositories.departments_repository import DepartmentsRepository

class CreateDepartmentUseCaseTest(TestCase):
    def setUp(self):
        self.departments_repository = DepartmentsRepository()
        self.use_case = CreateDepartmentUseCase(self.departments_repository)

    def test_create_department(self):
        data = {
            'name': 'Department Test',
            'description': 'Department Test Description',
        }

        department = self.use_case.execute(data)
        
        self.assertTrue(isinstance(department['id'], UUID))
        self.assertEqual(department['name'], "Department Test")
        self.assertTrue(department['created_at'] is not None)
        self.assertTrue(department['updated_at'] is None)

    def test_create_department_with_name_already_exists(self):
        data = {'name': 'Department Wrong'}
        with self.assertRaises(Exception) as context:
            self.use_case.execute(data)
            self.use_case.execute(data)

        self.assertIsInstance(context.exception, AppError)