from .search_projects_use_case import SearchProjectsUseCase
from src.modules.projects.repositories.projects_repository import ProjectsRepository

def make_search_projects_use_case():
    projects_repository = ProjectsRepository()

    use_case = SearchProjectsUseCase(projects_repository)

    return use_case