from .find_project_by_criteria_use_case import FindProjectByCriteriaUseCase
from src.modules.projects.repositories.projects_repository import ProjectsRepository

def make_find_project_by_criteria_use_case():
    projects_repository = ProjectsRepository()

    use_case = FindProjectByCriteriaUseCase(projects_repository)

    return use_case