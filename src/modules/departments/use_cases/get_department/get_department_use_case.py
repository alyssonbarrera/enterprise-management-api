from src.shared.errors.AppError import AppError
from src.utils.error_messages import DEPARTMENT_NOT_FOUND
from src.modules.departments.repositories.departments_repository import DepartmentsRepository

class GetDepartmentUseCase:
    def __init__(self, departments_repository: DepartmentsRepository):
        self.departments_repository = departments_repository
    
    def execute(self, id):
        department = self.departments_repository.get(id)

        if not department:
            raise AppError(DEPARTMENT_NOT_FOUND, 404)
        
        return department.to_dict()