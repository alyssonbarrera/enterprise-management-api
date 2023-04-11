from .create_department_and_employee import create_department_and_employee
from src.modules.projects.repositories.projects_repository import ProjectsRepository
from src.utils.date_converter import convert_date_to_datetime

def create_project(number=1):
    data = create_department_and_employee(number)
    department = data['Department']

    projects_repository = ProjectsRepository()

    project_data = {
        'name': f'Project Test {number}',
        'description': f'Project Test Description {number}',
        'department': department,
        'estimated_deadline': convert_date_to_datetime('15/04/2023'),
        'start_date': convert_date_to_datetime('10/04/2023'),
    }

    project = projects_repository.create(project_data)

    return project.to_dict()