from src.shared.errors.AppError import AppError
from src.utils.error_messages import PROJECT_NOT_FOUND
from ...repositories.projects_repository import ProjectsRepository
from src.utils.calculate_metrics import calculate_and_update_project_hours
from ....employees.repositories.employees_repository import EmployeesRepository
from ...repositories.projects_employees_repository import ProjectsEmployeesRepository

class RemoveEmployeesToProjectUseCase:
    def __init__(
            self,
            projects_repository: ProjectsRepository,
            employees_repository: EmployeesRepository,
            projects_employees_repository: ProjectsEmployeesRepository
        ):
        self.projects_repository = projects_repository
        self.employees_repository = employees_repository
        self.projects_employees_repository = projects_employees_repository

    def execute(self, project_id, employees):
        project = self.projects_repository.get(project_id)

        if project is None:
            raise AppError(PROJECT_NOT_FOUND, 404)

        for employee_id in employees:
            employee = self.employees_repository.get(employee_id)

            if employee is None:
                raise AppError(f'Employee with id {employee_id} not found', 404)

            self.projects_employees_repository.remove_employee_from_project(project, employee)

        calculate_and_update_project_hours(project)

        return project.to_dict()