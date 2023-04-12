from uuid import UUID
from django.test import TestCase
from src.shared.errors.AppError import AppError
from src.utils.date_converter import convert_date_to_datetime
from src.modules.projects.repositories.projects_repository import ProjectsRepository
from src.modules.employees.repositories.employees_repository import EmployeesRepository
from src.utils.test.create_department_and_employee import create_department_and_employee
from src.modules.departments.repositories.departments_repository import DepartmentsRepository
from src.modules.projects.use_cases.create_project.create_project_use_case import CreateProjectUseCase
from src.modules.projects.repositories.projects_employees_repository import ProjectsEmployeesRepository
from src.utils.error_messages import DEPARTMENT_NOT_FOUND, PROJECT_ALREADY_EXISTS_IN_DEPARTMENT

class CreateProjectUseCaseTest(TestCase):
    def setUp(self):
        self.projects_repository = ProjectsRepository()
        self.departments_repository = DepartmentsRepository()
        self.employees_repository = EmployeesRepository()
        self.projects_employees_repository = ProjectsEmployeesRepository()
        self.use_case = CreateProjectUseCase(
            self.projects_repository,
            self.departments_repository,
            self.employees_repository,
            self.projects_employees_repository
        )

    def test_create_project(self):
        data = create_department_and_employee()

        department = data['department']

        project_data = {
            'name': 'Project Test',
            'description': 'Project Test Description',
            'department': department['id'],
            'estimated_deadline': '20/04/2023'
        }

        project = self.use_case.execute(project_data)
        
        self.assertTrue(project['updated_at'] is None)
        self.assertTrue(isinstance(project['id'], UUID))
        self.assertEqual(project['name'], "Project Test")
        self.assertTrue(project['created_at'] is not None)

    def test_create_project_with_name_already_exists(self):
        data = create_department_and_employee()

        department = data['department']
        
        project_data_1 = {
            'name': 'Project Test',
            'description': 'Project Test Description',
            'department': department['id'],
            'estimated_deadline': '20/04/2023'
        }

        project_data_2 = {
            'name': 'Project Test',
            'description': 'Project Test Description',
            'department': department['id'],
            'estimated_deadline': '20/04/2023'
        }

        self.use_case.execute(project_data_1)

        with self.assertRaises(Exception) as context:
            self.use_case.execute(project_data_2)
        
        self.assertIsInstance(context.exception, AppError)
        self.assertEqual(context.exception.statusCode, 409)
        self.assertEqual(context.exception.message, PROJECT_ALREADY_EXISTS_IN_DEPARTMENT)

    def test_create_project_with_department_not_found(self):
        project_data = {
            'name': 'Project Test',
            'description': 'Project Test Description',
            'department': '00000000-0000-0000-0000-000000000000',
            'estimated_deadline': '20/04/2023'
        }

        with self.assertRaises(Exception) as context:
            self.use_case.execute(project_data)
        
        self.assertIsInstance(context.exception, AppError)
        self.assertEqual(context.exception.statusCode, 404)
        self.assertEqual(context.exception.message, DEPARTMENT_NOT_FOUND)

    def test_create_multiple_projects_in_department(self):
        data = create_department_and_employee()

        department = data['department']

        project_data_1 = {
            'name': 'Project Test 1',
            'description': 'Project Test Description 1',
            'department': department['id'],
            'estimated_deadline': '20/04/2023'
        }

        project_data_2 = {
            'name': 'Project Test 2',
            'description': 'Project Test Description 2',
            'department': department['id'],
            'estimated_deadline': '20/04/2023'
        }

        self.use_case.execute(project_data_1)
        project_2 = self.use_case.execute(project_data_2)

        self.assertTrue(project_2['updated_at'] is None)
        self.assertTrue(isinstance(project_2['id'], UUID))
        self.assertEqual(project_2['name'], "Project Test 2")
        self.assertTrue(project_2['created_at'] is not None)

    def test_create_project_with_employee(self):
        data = create_department_and_employee()

        department = data['department']
        employee = data['employee']

        project_data = {
            'name': 'Project Test',
            'description': 'Project Test Description',
            'department': department['id'],
            'employees': [employee['id']],
            'estimated_deadline': '15/04/2023'
        }

        project = self.use_case.execute(project_data)
        
        self.assertTrue(project['updated_at'] is None)
        self.assertTrue(isinstance(project['id'], UUID))
        self.assertEqual(project['name'], "Project Test")
        self.assertTrue(project['created_at'] is not None)
        self.assertEqual(project['employees'][0]['id'], employee['id'])

    def test_create_project_with_supervisor(self):
        data = create_department_and_employee()

        department = data['department']
        employee = data['employee']

        project_data = {
            'name': 'Project Test',
            'description': 'Project Test Description',
            'department': department['id'],
            'estimated_deadline': '15/04/2023',
            'supervisor': employee['id']
        }

        project = self.use_case.execute(project_data)
        
        self.assertTrue(project['updated_at'] is None)
        self.assertTrue(isinstance(project['id'], UUID))
        self.assertEqual(project['name'], "Project Test")
        self.assertTrue(project['created_at'] is not None)

    def test_create_project_with_supervisor_and_employee(self):
        data_1 = create_department_and_employee(1)
        data_2 = create_department_and_employee(2)

        department_1 = data_1['department']
        employee_1 = data_1['employee']

        employee_2 = data_2['employee']

        project_data = {
            'name': 'Project Test',
            'description': 'Project Test Description',
            'department': department_1['id'],
            'employees': [employee_1['id']],
            'estimated_deadline': '11/04/2023',
            'supervisor': employee_2['id']
        }

        project = self.use_case.execute(project_data)
        
        self.assertTrue(project['updated_at'] is None)
        self.assertTrue(isinstance(project['id'], UUID))
        self.assertEqual(project['name'], "Project Test")
        self.assertTrue(project['created_at'] is not None)
        self.assertEqual(project['employees'][0]['id'], employee_1['id'])

    def test_create_project_with_employee_not_found(self):
        data = create_department_and_employee()

        department = data['department']

        project_data = {
            'name': 'Project Test',
            'description': 'Project Test Description',
            'department': department['id'],
            'employees': ['00000000-0000-0000-0000-000000000001', '00000000-0000-0000-0000-000000000002', '00000000-0000-0000-0000-000000000003'],
            'estimated_deadline': '11/04/2023'
        }

        with self.assertRaises(Exception) as context:
            self.use_case.execute(project_data)
        
        self.assertIsInstance(context.exception, AppError)
        self.assertEqual(context.exception.statusCode, 404)

    def test_create_project_with_supervisor_has_no_hours(self):
        data = create_department_and_employee()

        department = data['department']
        employee = data['employee']

        project_data_1 = {
            'name': 'Project Test 1',
            'description': 'Project Test Description',
            'department': department['id'],
            'estimated_deadline': '11/04/2023',
            'supervisor': employee['id']
        }

        project_data_2 = {
            'name': 'Project Test 2',
            'description': 'Project Test Description',
            'department': department['id'],
            'estimated_deadline': '11/04/2023',
            'supervisor': employee['id']
        }

        self.use_case.execute(project_data_1)
        
        with self.assertRaises(Exception) as context:
            self.use_case.execute(project_data_2)
        self.assertIsInstance(context.exception, AppError)
        self.assertEqual(context.exception.statusCode, 409)

    def test_create_project_with_employee_has_no_hours(self):
        data = create_department_and_employee()

        department = data['department']
        employee = data['employee']

        project_data_1 = {
            'name': 'Project Test 1',
            'description': 'Project Test Description',
            'department': department['id'],
            'estimated_deadline': '11/04/2023',
            'employees': [employee['id']]
        }

        project_data_2 = {
            'name': 'Project Test 2',
            'description': 'Project Test Description',
            'department': department['id'],
            'estimated_deadline': '11/04/2023',
            'employees': [employee['id']]
        }

        self.use_case.execute(project_data_1)
        
        with self.assertRaises(Exception) as context:
            self.use_case.execute(project_data_2)
        self.assertIsInstance(context.exception, AppError)
        self.assertEqual(context.exception.statusCode, 409)

    def test_create_project_finished(self):
        data = create_department_and_employee()
        data_2 = create_department_and_employee(2)

        department = data['department']
        employee = data['employee']

        employee_2 = data_2['employee']

        project_data = {
            'name': 'Project Test',
            'description': 'Project Test Description',
            'department': department['id'],
            'employees': [employee['id']],
            'estimated_deadline': '15/04/2023',
            'supervisor': employee_2['id'],
            'start_date': '10/02/2023',
            'end_date': '15/02/2023',
            'done': True,
            'last_hours_calculation_date': '02/04/2023',
            'completed_hours': 100,
        }

        project = self.use_case.execute(project_data)
        project_employee = self.projects_employees_repository.get_by_project(project['id'])

        self.assertTrue(project['updated_at'] is None)
        self.assertTrue(isinstance(project['id'], UUID))
        self.assertEqual(project['name'], "Project Test")
        self.assertTrue(project['created_at'] is not None)
        self.assertTrue(project['remaining_hours'] == 0)
        self.assertEqual(project['employees'], [])
        self.assertTrue(project['done'] == True)
        self.assertEqual(project_employee, [])
