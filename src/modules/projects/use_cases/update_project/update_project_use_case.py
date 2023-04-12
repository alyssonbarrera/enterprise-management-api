from datetime import datetime
from django.utils import timezone
from src.shared.errors.AppError import AppError
from src.utils.date_converter import convert_date_to_datetime
from src.shared.errors.DuplicateEntryError import DuplicateEntryError
from src.utils.calculate_metrics import calculate_and_update_project_hours
from src.utils.employee_available_work_hours import employee_available_work_hours
from src.modules.projects.repositories.projects_repository import ProjectsRepository
from src.modules.employees.repositories.employees_repository import EmployeesRepository
from src.modules.departments.repositories.departments_repository import DepartmentsRepository
from src.modules.projects.repositories.projects_employees_repository import ProjectsEmployeesRepository
from src.utils.error_messages import PROJECT_NOT_FOUND, DEPARTMENT_NOT_FOUND, PROJECT_ALREADY_EXISTS_IN_DEPARTMENT

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

        try:
            project = self.projects_repository.get(id)

            if not project:
                raise AppError(PROJECT_NOT_FOUND, 404)

            department = project.department

            if 'department' in data:
                department = self.departments_repository.get(data['department'])

                if not department:
                    raise AppError(DEPARTMENT_NOT_FOUND, 404)

            if 'name' in data and project.name != data['name']:
                department_already_has_project_with_same_name = self.projects_repository.project_already_exists_in_department(data['name'])

                if department_already_has_project_with_same_name:
                    raise AppError(PROJECT_ALREADY_EXISTS_IN_DEPARTMENT, 409)

            data['department'] = department

            data['estimated_deadline'] = convert_date_to_datetime(data['estimated_deadline']) if 'estimated_deadline' in data else project.estimated_deadline
            data['start_date'] = convert_date_to_datetime(data['start_date']) if 'start_date' in data else project.start_date
            data['end_date'] = convert_date_to_datetime(data['end_date']) if 'end_date' in data else project.end_date
            data['last_hours_calculation_date'] = convert_date_to_datetime(data['last_hours_calculation_date']) if 'last_hours_calculation_date' in data else project.last_hours_calculation_date

            employees_not_found = []

            if 'employees' in data:
                for employee_id in data['employees']:
                    employee = self.employees_repository.get(employee_id)

                    if not employee:
                        employees_not_found.append(employee_id)
                        continue

                    employees_data.append(employee)

                if employees_not_found:
                    raise AppError(f"Employees with ids {', '.join(map(str, employees_not_found))} not found", 404)

                del data['employees']

            if 'supervisor' in data:
                supervisor = self.employees_repository.get(data['supervisor'])

                if not supervisor:
                    raise AppError(f'Supervisor with id {data["supervisor"]} not found', 404)
                            
                if project.supervisor is not None and supervisor.id == project.supervisor.id:
                    raise AppError(f'Supervisor with id {data["supervisor"]} is already the supervisor of this project', 409)
                
                supervisor_data = supervisor
                data['supervisor'] = supervisor

            data['updated_at'] = timezone.now()

            if employees_data:
                self.projects_employees_repository.delete_employees_from_project(project)

                for employee in employees_data:
                    hours_available_by_employee = employee_available_work_hours(employee, self.projects_employees_repository)
                    
                    employee = {
                        'employee': employee,
                        'hours_worked_per_week': hours_available_by_employee
                    }

                    self.projects_employees_repository.add_employee_to_project(project, employee)

            if supervisor_data:
                hours_available_by_supervisor = employee_available_work_hours(supervisor_data, self.projects_employees_repository)
                
                supervisor = {
                    'supervisor': supervisor_data,
                    'hours_worked_per_week': hours_available_by_supervisor
                }

                self.projects_employees_repository.replace_supervisor_in_project(project, supervisor)

            if 'done' in data:
                if data['done'] == True:
                    data['end_date'] = datetime.now()

                    self.projects_employees_repository.delete(project)
                else:
                    data['end_date'] = None                

            project_updated = self.projects_repository.update(project, data)

            calculate_and_update_project_hours(project_updated)

            return project_updated.to_dict()
        except DuplicateEntryError as error:
            raise AppError(error.message, error.statusCode)