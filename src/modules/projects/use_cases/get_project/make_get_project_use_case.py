from .get_project_use_case import GetProjectUseCase
from src.modules.projects.repositories.projects_repository import ProjectsRepository

def make_get_project_use_case():
    projects_repository = ProjectsRepository()

    use_case = GetProjectUseCase(projects_repository)

    return use_case