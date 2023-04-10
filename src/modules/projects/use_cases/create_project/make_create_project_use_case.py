from .create_project_use_case import CreateProjectUseCase
from src.modules.projects.repositories.projects_repository import ProjectsRepository
from src.modules.employees.repositories.employees_repository import EmployeesRepository
from src.modules.departments.repositories.departments_repository import DepartmentsRepository
from src.modules.projects.repositories.projects_employees_repository import ProjectsEmployeesRepository

def make_create_project_use_case():
    projects_repository = ProjectsRepository()
    departments_repository = DepartmentsRepository()
    employees_repository = EmployeesRepository()
    projects_employees_repository = ProjectsEmployeesRepository()

    use_case = CreateProjectUseCase(
        projects_repository,
        departments_repository,
        employees_repository,
        projects_employees_repository
    )

    return use_case