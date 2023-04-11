from src.shared.errors.AppError import AppError
from src.utils.error_messages import PROJECT_NOT_FOUND
from ...repositories.projects_repository import ProjectsRepository
from src.utils.calculate_metrics import calculate_available_work_hours
from src.utils.calculate_metrics import calculate_and_update_project_hours
from ....employees.repositories.employees_repository import EmployeesRepository
from ...repositories.projects_employees_repository import ProjectsEmployeesRepository

class AddEmployeesToProjectUseCase:
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

            hours_available_by_employee = calculate_available_work_hours(employee, self.projects_employees_repository)

            if hours_available_by_employee == 0:
                raise AppError(f'Employee {employee.name} has no hours available', 409)

            employee_data = ({
                'employee': employee,
                'hours_worked_per_week': hours_available_by_employee
            })

            self.projects_employees_repository.add_employee_to_project(project, employee_data)

        calculate_and_update_project_hours(project)

        return project.to_dict()