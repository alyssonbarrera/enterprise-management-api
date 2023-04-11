from unittest.mock import patch
from django.test import TestCase
from src.shared.errors.AppError import AppError
from ....repositories.departments_repository import DepartmentsRepository
from ...delete_department.delete_department_use_case import DeleteDepartmentUseCase
from src.utils.error_messages import DEPARTMENT_NOT_FOUND, DEPARTMENT_HAS_ACTIVE_EMPLOYEES, DEPARTMENT_HAS_ACTIVE_PROJECTS

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

    def test_delete_nonexistent_department(self):
        data = {
            'name': 'Department Test',
            'description': 'Department Test Description',
        }
        
        department = self.departments_repository.create(data).to_dict()

        self.use_case.execute(department['id'])

        with self.assertRaises(Exception) as context:
            self.use_case.execute(department['id'])

        self.assertIsInstance(context.exception, AppError)
        self.assertEqual(context.exception.message, DEPARTMENT_NOT_FOUND)

    def test_delete_department_with_active_employees(self):
        data = {
            'name': 'Department Test',
            'description': 'Department Test Description',
        }
        
        department = self.departments_repository.create(data)
        department_dict = department.to_dict()

        with patch.object(self.departments_repository, 'has_active_employees', return_value=True):
            with self.assertRaises(Exception) as context:
                self.use_case.execute(department_dict['id'])

        self.assertIsInstance(context.exception, AppError)
        self.assertEqual(context.exception.message, DEPARTMENT_HAS_ACTIVE_EMPLOYEES)

    def test_delete_department_with_active_projects(self):
        data = {
            'name': 'Department Test',
            'description': 'Department Test Description',
        }
        
        department = self.departments_repository.create(data)
        department_dict = department.to_dict()

        with patch.object(self.departments_repository, 'has_active_projects', return_value=True):
            with self.assertRaises(Exception) as context:
                self.use_case.execute(department_dict['id'])

        self.assertIsInstance(context.exception, AppError)
        self.assertEqual(context.exception.message, DEPARTMENT_HAS_ACTIVE_PROJECTS)