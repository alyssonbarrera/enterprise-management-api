from .get_all_projects_use_case import GetAllProjectsUseCase
from src.modules.projects.repositories.projects_repository import ProjectsRepository

def make_get_all_projects_use_case():
    projects_repository = ProjectsRepository()

    use_case = GetAllProjectsUseCase(projects_repository)

    return use_case
