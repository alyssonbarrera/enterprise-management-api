from django.utils import timezone
from src.shared.errors.AppError import AppError
from src.utils.error_messages import DEPARTMENT_NOT_FOUND, DEPARTMENT_ALREADY_EXISTS
from src.modules.departments.repositories.departments_repository import DepartmentsRepository

class UpdateDepartmentUseCase:
    def __init__(self, departments_repository: DepartmentsRepository):
        self.departments_repository = departments_repository

    def execute(self, id, data):
        department = self.departments_repository.get(id)

        if not department:
            raise AppError(DEPARTMENT_NOT_FOUND, 404)

        if 'name' in data:
            department_with_same_name = self.departments_repository.get_by_name(data['name'])

            if department_with_same_name:
                raise AppError(DEPARTMENT_ALREADY_EXISTS, 409)
            

        data['updated_at'] = timezone.now()
        
        department = self.departments_repository.update(id, data)
        
        return department.to_dict()