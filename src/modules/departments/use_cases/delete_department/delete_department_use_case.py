from src.shared.errors.AppError import AppError
from src.utils.error_messages import DEPARTMENT_NOT_FOUND, DEPARTMENT_HAS_ACTIVE_EMPLOYEES, DEPARTMENT_HAS_ACTIVE_PROJECTS
from src.modules.departments.repositories.departments_repository import DepartmentsRepository

class DeleteDepartmentUseCase:
    def __init__(self, departments_repository: DepartmentsRepository):
        self.departments_repository = departments_repository

    def execute(self, id):
        department = self.departments_repository.get(id)

        if not department:
            raise AppError(DEPARTMENT_NOT_FOUND, 404)
        
        exists_active_employees = self.departments_repository.has_active_employees(id)
        exists_active_projects = self.departments_repository.has_active_projects(id)
        
        if exists_active_employees:
            raise AppError(DEPARTMENT_HAS_ACTIVE_EMPLOYEES, 400)
        
        if exists_active_projects:
            raise AppError(DEPARTMENT_HAS_ACTIVE_PROJECTS, 400)

        self.departments_repository.delete(department)