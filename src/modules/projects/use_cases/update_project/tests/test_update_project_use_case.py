from unittest.mock import patch
from django.test import TestCase
from src.shared.errors.AppError import AppError
from src.shared.infra.database.models import Department
from src.utils.test.create_project import create_project
from src.utils.test.create_department import create_department
from ....repositories.projects_repository import ProjectsRepository
from ...update_project.update_project_use_case import UpdateProjectUseCase
from src.utils.error_messages import PROJECT_NOT_FOUND, DEPARTMENT_NOT_FOUND
from .....employees.repositories.employees_repository import EmployeesRepository
from src.utils.test.create_project_with_employee import create_project_with_employee
from ....repositories.projects_employees_repository import ProjectsEmployeesRepository
from .....departments.repositories.departments_repository import DepartmentsRepository
from src.utils.test.create_department_and_employee import create_department_and_employee

class UpdateProjectUseCaseTest(TestCase):
    def setUp(self):
        self.projects_repository = ProjectsRepository()
        self.departments_repository = DepartmentsRepository()
        self.employees_repository = EmployeesRepository()
        self.projects_employees_repository = ProjectsEmployeesRepository()
        
        self.use_case = UpdateProjectUseCase(
            self.projects_repository,
            self.departments_repository,
            self.employees_repository,
            self.projects_employees_repository
        )

    def test_update_project(self):
        project = create_project(5)

        project_data = {
            'name': 'Project Test 2',
            'description': 'Project Test Description 2',
        }

        updated_project = self.use_case.execute(project['id'], project_data)

        self.assertEqual(updated_project['name'], project_data['name'])
        self.assertEqual(updated_project['description'], project_data['description'])

    def test_update_project_if_not_exists(self):
        project_data = {
            'name': 'Project Test 2',
            'description': 'Project Test Description 2',
        }

        with self.assertRaises(Exception) as context:
            self.use_case.execute('00000000-0000-0000-0000-000000000000', project_data)

        self.assertIsInstance(context.exception, AppError)
        self.assertEqual(context.exception.message, PROJECT_NOT_FOUND)

    def test_update_project_name_already_exists_in_department(self):
        project = create_project()

        project_data = {
            'name': 'Project Test 2',
        }

        with patch.object(self.projects_repository, 'project_already_exists_in_department', return_value=True):
            with self.assertRaises(Exception):
                self.use_case.execute(project['id'], project_data)
                
    def test_update_project_with_department_not_exists(self):
        project = create_project()

        project_data = {
            'name': 'Project Test 2',
            'description': 'Project Test Description 2',
            'department': '00000000-0000-0000-0000-000000000000',
        }

        with self.assertRaises(Exception) as context:
            self.use_case.execute(project['id'], project_data)

        self.assertIsInstance(context.exception, AppError)
        self.assertEqual(context.exception.message, DEPARTMENT_NOT_FOUND)

    def test_update_project_with_department(self):
        department = create_department(2)

        project = create_project()

        project_data = {
            'name': 'Project Test 2',
            'description': 'Project Test Description 2',
            'department': department['department']['id'],
        }

        updated_project = self.use_case.execute(project['id'], project_data)

        self.assertEqual(updated_project['name'], project_data['name'])
        self.assertEqual(updated_project['description'], project_data['description'])
        self.assertEqual(updated_project['department']['id'], department['department']['id'])

    def test_update_project_with_employee(self):
        data = create_department_and_employee(4)
        data_2 = create_department_and_employee(5)

        employee = data['employee']
        employee_2 = data_2['employee']

        project = create_project()

        project_data = {
            'name': 'Project Test 2',
            'description': 'Project Test Description 2',
            'employees': [employee['id'], data_2['employee']['id']],
        }

        updated_project = self.use_case.execute(project['id'], project_data)
        project_employee = self.projects_employees_repository.get_by_project(project['id'])

        self.assertEqual(updated_project['name'], project_data['name'])
        self.assertEqual(updated_project['description'], project_data['description'])
        self.assertEqual(updated_project['employees'][0]['id'], employee['id'])
        self.assertEqual(updated_project['employees'][1]['id'], employee_2['id'])
        self.assertEqual(project_employee[0]['employee'], employee['id'])
        self.assertEqual(project_employee[1]['employee'], employee_2['id'])

    def test_update_project_with_employee_and_department(self):
        data = create_department_and_employee(5)
        data_2 = create_department_and_employee(6)

        employee = data['employee']
        employee_2 = data_2['employee']
        department = data['department']

        project = create_project()

        project_data = {
            'name': 'Project Test 2',
            'description': 'Project Test Description 2',
            'employees': [employee['id'], employee_2['id']],
            'department': department['id'],
        }

        updated_project = self.use_case.execute(project['id'], project_data)

        self.assertEqual(updated_project['name'], project_data['name'])
        self.assertEqual(updated_project['description'], project_data['description'])
        self.assertEqual(updated_project['employees'][0]['id'], employee['id'])
        self.assertEqual(updated_project['department']['id'], department['id'])

    def test_update_project_with_supervisor(self):
        data = create_department_and_employee(6)

        project = create_project()
        employee = data['employee']

        project_data = {
            'name': 'Project Test 2',
            'description': 'Project Test Description 2',
            'supervisor': employee['id'],
        }

        updated_project = self.use_case.execute(project['id'], project_data)

        self.assertEqual(updated_project['name'], project_data['name'])
        self.assertEqual(updated_project['description'], project_data['description'])
        self.assertEqual(updated_project['supervisor']['id'], employee['id'])

    def test_update_project_with_supervisor_and_department(self):
        data = create_department_and_employee(7)

        project = create_project()
        employee = data['employee']
        department = data['department']

        project_data = {
            'name': 'Project Test 2',
            'description': 'Project Test Description 2',
            'supervisor': employee['id'],
            'department': department['id'],
        }

        updated_project = self.use_case.execute(project['id'], project_data)

        self.assertEqual(updated_project['name'], project_data['name'])
        self.assertEqual(updated_project['description'], project_data['description'])
        self.assertEqual(updated_project['supervisor']['id'], employee['id'])
        self.assertEqual(updated_project['department']['id'], department['id'])

    def test_update_project_with_employee_has_no_hours(self):
        data = create_department_and_employee(8)
        project = create_project()

        employee = data['employee']
        project_data = {
            'name': 'Project Test 2',
            'description': 'Project Test Description 2',
            'employees': [employee['id'], employee['id']],
        }


        with self.assertRaises(Exception) as context:
            self.use_case.execute(project['id'], project_data)

        self.assertIsInstance(context.exception, AppError)
    
    def test_update_project_with_supervisor_has_no_hours(self):
        data = create_department_and_employee(9)
        project = create_project()

        employee = data['employee']
        project_data = {
            'name': 'Project Test 2',
            'description': 'Project Test Description 2',
            'employees': [employee['id']],
            'supervisor': employee['id'],
        }

        with self.assertRaises(Exception) as context:
            self.use_case.execute(project['id'], project_data)

        self.assertIsInstance(context.exception, AppError)
    
    def test_update_project_done(self):
        project = create_project_with_employee()

        project_data = {
            'done': True,
        }

        updated_project = self.use_case.execute(project['id'], project_data)
        project_employees = self.projects_employees_repository.get_by_project(project['id'])

        self.assertEqual(updated_project['done'], project_data['done'])
        self.assertEqual(updated_project['employees'], [])
        self.assertEqual(project_employees, [])