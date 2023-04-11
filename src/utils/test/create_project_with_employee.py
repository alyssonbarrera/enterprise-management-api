from src.utils.date_converter import convert_date_to_datetime
from .create_department_and_employee import create_department_and_employee
from src.modules.projects.repositories.projects_repository import ProjectsRepository
from src.modules.projects.repositories.projects_employees_repository import ProjectsEmployeesRepository

def create_project_with_employee(number=1):
    data = create_department_and_employee(number)
    department = data['Department']
    employee = data['employee']

    projects_repository = ProjectsRepository()
    projects_employees_repository = ProjectsEmployeesRepository()

    project_data = {
        'name': f'Project Test {number}',
        'description': f'Project Test Description {number}',
        'department': department,
        'estimated_deadline': convert_date_to_datetime('15/04/2023'),
    }

    employee_data = {
        'employee': employee['id'],
        'hours_worked_per_week': 40,
    }

    project = projects_repository.create(project_data)
    projects_employees_repository.add_employee_to_project(project, employee_data)

    return project.to_dict()