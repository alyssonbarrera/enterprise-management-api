from src.shared.errors.AppError import AppError
from src.utils.error_messages import PROJECT_NOT_FOUND
from src.modules.projects.repositories.projects_repository import ProjectsRepository

class DeleteProjectUseCase:
    def __init__(self, projects_repository: ProjectsRepository):
        self.projects_repository = projects_repository

    def execute(self, id):
        project = self.projects_repository.get(id)

        if not project:
            raise AppError(PROJECT_NOT_FOUND, 404)
        
        self.projects_repository.delete(project)