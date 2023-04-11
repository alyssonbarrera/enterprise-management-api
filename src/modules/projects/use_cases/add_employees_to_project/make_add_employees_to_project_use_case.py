from .add_employees_to_project_use_case import AddEmployeesToProjectUseCase
from src.modules.projects.repositories.projects_repository import ProjectsRepository
from src.modules.employees.repositories.employees_repository import EmployeesRepository
from src.modules.projects.repositories.projects_employees_repository import ProjectsEmployeesRepository

def make_add_employees_to_project_use_case():
    projects_repository = ProjectsRepository()
    employees_repository = EmployeesRepository()
    projects_employees_repository = ProjectsEmployeesRepository()

    use_case = AddEmployeesToProjectUseCase(
        projects_repository,
        employees_repository,
        projects_employees_repository
    )

    return use_case