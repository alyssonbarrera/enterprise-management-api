from .delete_project_use_case import DeleteProjectUseCase
from src.modules.projects.repositories.projects_repository import ProjectsRepository

def make_delete_project_use_case():
    projects_repository = ProjectsRepository()

    use_case = DeleteProjectUseCase(projects_repository)

    return use_case
