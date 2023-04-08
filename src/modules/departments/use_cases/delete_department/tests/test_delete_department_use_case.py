from django.test import TestCase
from src.shared.errors.AppError import AppError
from ....repositories.departments_repository import DepartmentsRepository
from ...delete_department.delete_department_use_case import DeleteDepartmentUseCase

class DeleteDepartmentUseCaseTest(TestCase):
    def setUp(self):
        self.departments_repository = DepartmentsRepository()
        self.use_case = DeleteDepartmentUseCase(self.departments_repository)

    def test_delete_department(self):
        data = {
            'name': 'Department Test',
            'description': 'Department Test Description',
        }
        
        department = self.departments_repository.create(data).to_dict()

        self.use_case.execute(department['id'])
        
        get_department = self.departments_repository.get(department['id'])
        
        self.assertEqual(get_department, None)

    def test_delete_department_with_id_not_exists(self):
        with self.assertRaises(Exception) as context:
            self.use_case.execute('00000000-0000-0000-0000-000000000000')

        self.assertIsInstance(context.exception, AppError)