from src.modules.projects.repositories.projects_repository import ProjectsRepository
from src.shared.errors.AppError import AppError
from src.utils.error_messages import PROJECT_NOT_FOUND

class FindProjectByCriteriaUseCase:
    def __init__(self, projects_repository: ProjectsRepository):
        self.projects_repository = projects_repository

    def execute(self, criteria):
        project = self.projects_repository.find_by_criteria(criteria)

        if not project:
            raise AppError(PROJECT_NOT_FOUND, 404)
        
        return project.to_dict()