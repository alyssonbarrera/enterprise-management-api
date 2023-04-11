from src.shared.errors.AppError import AppError
from src.utils.error_messages import PROJECT_NOT_FOUND
from ...repositories.projects_repository import ProjectsRepository
from src.utils.calculate_metrics import calculate_and_update_project_hours

class FetchProjectMetricsUseCase:
    def __init__(self, projects_repository: ProjectsRepository):
        self.projects_repository = projects_repository

    def execute(self, project_id):
        project = self.projects_repository.get(project_id)

        if not project:
            raise AppError(PROJECT_NOT_FOUND, 404)
        
        calculate_and_update_project_hours(project)
        
        project_dict = project.to_dict()

        return {
            'id': project_dict['id'],
            'name': project_dict['name'],
            'description': project_dict['description'],
            'remaining_hours': project_dict['remaining_hours'],
            'completed_hours': project_dict['completed_hours'],
            'estimated_deadline': project_dict['estimated_deadline'],
            'last_hours_calculation_date': project_dict['last_hours_calculation_date'],
            'num_employees': len(project_dict['employees']),
            'start_date': project_dict['start_date'],
            'end_date': project_dict['end_date'],
            'done': project_dict['done'],
        }