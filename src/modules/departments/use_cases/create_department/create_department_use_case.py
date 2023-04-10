from src.shared.errors.AppError import AppError
from src.utils.error_messages import DEPARTMENT_ALREADY_EXISTS
from src.modules.departments.repositories.departments_repository import DepartmentsRepository

class CreateDepartmentUseCase:
    def __init__(self, departments_repository: DepartmentsRepository):
        self.departments_repository = departments_repository

    def execute(self, data):
        departmentAlreadyExists = self.departments_repository.get_by_name(data['name'])

        if departmentAlreadyExists:
            raise AppError(DEPARTMENT_ALREADY_EXISTS, 409)

        department = self.departments_repository.create(data)
        
        return department.to_dict()