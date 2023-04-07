from src.shared.errors.AppError import AppError
from src.modules.departments.repositories.departments_repository import DepartmentsRepository

class DeleteDepartmentUseCase:
    def __init__(self, departments_repository: DepartmentsRepository):
        self.departments_repository = departments_repository

    def execute(self, id):
        department = self.departments_repository.get(id)

        if not department:
            raise AppError('Department not found', 404)

        self.departments_repository.delete(id)