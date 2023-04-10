from django.test import TestCase
from src.shared.errors.AppError import AppError
from src.utils.error_messages import DEPARTMENT_NOT_FOUND
from ....repositories.departments_repository import DepartmentsRepository
from ...get_department.get_department_use_case import GetDepartmentUseCase

class GetDepartmentUseCaseTest(TestCase):
    def setUp(self):
        self.departments_repository = DepartmentsRepository()
        self.use_case = GetDepartmentUseCase(self.departments_repository)

    def test_get_department(self):
        data = {
            'name': 'Department Test 1',
            'description': 'Department Test Description 1',
        }

        create_department = self.departments_repository.create(data).to_dict()

        department = self.use_case.execute(create_department['id'])

        self.assertEqual(department['id'], create_department['id'])

    def test_get_department_if_not_exists(self):
        with self.assertRaises(Exception) as context:
            self.use_case.execute('00000000-0000-0000-0000-000000000000')
        self.assertIsInstance(context.exception, AppError)
        self.assertEqual(context.exception.message, DEPARTMENT_NOT_FOUND)