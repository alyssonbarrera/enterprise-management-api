from uuid import UUID
from django.test import TestCase
from src.shared.errors.AppError import AppError
from src.modules.departments.use_cases.create_department.create_department_use_case import CreateDepartmentUseCase
from src.modules.departments.use_cases.create_department.make_create_department_use_case import make_create_department_use_case

class DepartmentUseCaseTest(TestCase):
    def setUp(self):
        self.create_department_use_case = make_create_department_use_case()

    def test_create_department(self):
        data = {'name': 'Department 1'}
        department = self.create_department_use_case.execute(data)
        self.assertTrue(isinstance(department['id'], UUID))
        self.assertEqual(department['name'], "Department 1")
        self.assertTrue(department['created_at'] is not None)
        self.assertTrue(department['updated_at'] is None)

    def test_create_department_with_name_already_exists(self):
        data = {'name': 'Department 1'}
        with self.assertRaises(Exception) as context:
            self.create_department_use_case.execute(data)
            self.create_department_use_case.execute(data)

        self.assertIsInstance(context.exception, AppError)