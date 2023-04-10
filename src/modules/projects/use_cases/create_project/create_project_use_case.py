from datetime import datetime
from src.shared.errors.AppError import AppError
from src.utils.date_converter import convert_date_to_datetime
from ...repositories.projects_repository import ProjectsRepository
from src.shared.errors.DuplicateEntryError import DuplicateEntryError
from ....employees.repositories.employees_repository import EmployeesRepository
from ....departments.repositories.departments_repository import DepartmentsRepository
from ....projects.repositories.projects_employees_repository import ProjectsEmployeesRepository
from src.utils.error_messages import DEPARTMENT_NOT_FOUND, PROJECT_ALREADY_EXISTS_IN_DEPARTMENT
from src.utils.calculate_metrics import calculate_remaining_hours, calculate_available_work_hours, calculate_completed_hours, calculate_project_hours

class CreateProjectUseCase:
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

    def execute(self, project_data):
        employees_project_data = []
        supervisor_project_data = None
        
        department = self.departments_repository.get(project_data['department'])

        if not department:
            raise AppError(DEPARTMENT_NOT_FOUND, 404)
                
        project_data['department'] = department # department should be an instance of Department entity
        
        project_already_exists_in_department = self.projects_repository.project_already_exists_in_department(project_data['name'])

        if project_already_exists_in_department:
            raise AppError(PROJECT_ALREADY_EXISTS_IN_DEPARTMENT, 409)
        
        project_data['last_hours_calculation_date'] = convert_date_to_datetime(project_data['last_hours_calculation_date']) if 'last_hours_calculation_date' in project_data else datetime.now()
        project_data['estimated_deadline'] = convert_date_to_datetime(project_data['estimated_deadline'])
        project_data['completed_hours'] = project_data['completed_hours'] if 'completed_hours' in project_data else 0
        project_data['start_date'] = convert_date_to_datetime(project_data['start_date']) if 'start_date' in project_data else datetime.now()
        project_data['end_date'] = convert_date_to_datetime(project_data['end_date']) if 'end_date' in project_data else None
        project_data['remaining_hours'] = calculate_remaining_hours(project_data)
        project_data['done'] = project_data['done'] if 'done' in project_data else False
        
        if 'employees' in project_data:
            for employee_id in project_data['employees']:
                employee = self.employees_repository.get(employee_id)

                if not employee:
                    raise AppError(f'Employee with id {employee_id} not found', 404)

                employees_project_data.append(employee)
            del project_data['employees']

        if 'supervisor' in project_data:
            supervisor = self.employees_repository.get(project_data['supervisor'])

            if not supervisor:
                raise AppError(f'Supervisor with id {project_data["supervisor"]} not found', 404)
            
            supervisor_project_data = supervisor # supervisor should be an instance of Employee entity
            del project_data['supervisor']

        try:
            project = self.projects_repository.create(project_data)

            if employees_project_data:
                for employee in employees_project_data:
                    hours_available_by_employee = calculate_available_work_hours(employee, self.projects_employees_repository)

                    if hours_available_by_employee == 0:
                        raise AppError(f'Employee {employee.name} has no available hours to work on this project', 409)

                    employee_data = []
                    employee_data.append({
                        'employee': employee,
                        'hours_worked_per_week': hours_available_by_employee
                    })
                    
                    self.projects_employees_repository.add_employees_to_project(project, employee_data)

            if supervisor_project_data:
                hours_available_by_supervisor = calculate_available_work_hours(supervisor_project_data, self.projects_employees_repository)

                if hours_available_by_supervisor == 0:
                    raise AppError(f'Supervisor {supervisor_project_data.name} has no available hours to work on this project', 409)

                supervisor_data = {
                    'supervisor': supervisor_project_data,
                    'hours_worked_per_week': hours_available_by_supervisor
                }

                self.projects_employees_repository.add_supervisor_to_project(project, supervisor_data)

            if 'start_date' in project_data:
                calculate_project_hours(project)

            return project.to_dict()
        except DuplicateEntryError as error:
            raise AppError(error.message, error.statusCode)
