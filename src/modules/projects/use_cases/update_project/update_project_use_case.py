from django.utils import timezone
from src.shared.errors.AppError import AppError
from src.shared.errors.DuplicateEntryError import DuplicateEntryError
from src.modules.projects.repositories.projects_repository import ProjectsRepository
from src.modules.employees.repositories.employees_repository import EmployeesRepository
from src.modules.departments.repositories.departments_repository import DepartmentsRepository
from src.modules.projects.repositories.projects_employees_repository import ProjectsEmployeesRepository
from src.utils.error_messages import PROJECT_NOT_FOUND, DEPARTMENT_NOT_FOUND, PROJECT_ALREADY_EXISTS_IN_DEPARTMENT
from src.utils.calculate_metrics import calculate_available_work_hours, calculate_and_update_project_hours

class UpdateProjectUseCase:
    def __init__(
            self,
            projects_repository: ProjectsRepository,
            departments_repository: DepartmentsRepository,
            employees_repository: EmployeesRepository,
            projects_employees_repository: ProjectsEmployeesRepository
        ):
        self.projects_repository = projects_repository
        self.departments_repository = departments_repository
        self.employees_repository = employees_repository
        self.projects_employees_repository = projects_employees_repository

    def execute(self, id, data):
        employees_data = []
        supervisor_data = None

        project = self.projects_repository.get(id)

        if not project:
            raise AppError(PROJECT_NOT_FOUND, 404)

        department = project.department

        if 'department' in data:
            department = self.departments_repository.get(data['department'])

            if not department:
                raise AppError(DEPARTMENT_NOT_FOUND, 404)

        if project.name != data['name']:
            department_already_has_project_with_same_name = self.projects_repository.project_already_exists_in_department(data['name'])

            if department_already_has_project_with_same_name:
                raise AppError(PROJECT_ALREADY_EXISTS_IN_DEPARTMENT, 409)

        data['department'] = department
        
        if 'employees' in data:
            for employee_id in data['employees']:
                employee = self.employees_repository.get(employee_id)

                if not employee:
                    raise AppError(f'Employee with id {employee_id} not found', 404)

                employees_data.append(employee)
            del data['employees']

        if 'supervisor' in data:
            supervisor = self.employees_repository.get(data['supervisor'])

            if not supervisor:
                raise AppError(f'Supervisor with id {data["supervisor"]} not found', 404)

            supervisor_data = supervisor
            data['supervisor'] = supervisor

        data['updated_at'] = timezone.now()
        
        try:
            project = self.projects_repository.update(id, data)

            if employees_data:
                self.projects_employees_repository.delete_employees_from_project(project)

                for employee in employees_data:
                    hours_available_by_employee = calculate_available_work_hours(employee, self.projects_employees_repository)

                    if hours_available_by_employee == 0:
                        raise AppError(f'Employee {employee.name} has no available work hours', 409)
                    
                    employee = {
                        'employee': employee,
                        'hours_worked_per_week': hours_available_by_employee
                    }

                    self.projects_employees_repository.add_employee_to_project(project, employee)

            if supervisor_data:
                hours_available_by_supervisor = calculate_available_work_hours(supervisor_data, self.projects_employees_repository)

                if hours_available_by_supervisor == 0:
                    raise AppError(f'Supervisor {supervisor_data.name} has no available work hours', 409)
                
                supervisor = {
                    'supervisor': supervisor_data,
                    'hours_worked_per_week': hours_available_by_supervisor
                }
                
                self.projects_employees_repository.replace_supervisor_in_project(project, supervisor)
                
            calculate_and_update_project_hours(project)

            return project.to_dict()
        except DuplicateEntryError as error:
            raise AppError(error.message, error.statusCode)