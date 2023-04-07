from src.shared.errors.AppError import AppError
from src.modules.departments.repositories.departments_repository import DepartmentsRepository

class CreateDepartmentUseCase:
    def __init__(self, departments_repository: DepartmentsRepository):
        self.departments_repository = departments_repository

    def execute(self, data):
        departmentAlreadyExists = self.departments_repository.get_by_name(data['name'])

        if departmentAlreadyExists:
            raise AppError('Department already exists', 409)

        department = self.departments_repository.create(data)
        
        return department