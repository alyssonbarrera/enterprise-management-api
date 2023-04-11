from ...repositories.projects_repository import ProjectsRepository
from .fetch_project_metrics_use_case import FetchProjectMetricsUseCase

def make_fetch_project_metrics_use_case():
    projects_repository = ProjectsRepository()
    
    use_case = FetchProjectMetricsUseCase(projects_repository)

    return use_case