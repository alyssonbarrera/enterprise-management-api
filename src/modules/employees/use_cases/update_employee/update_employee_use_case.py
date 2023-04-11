from django.utils import timezone
from src.shared.errors.AppError import AppError
from src.utils.error_messages import EMPLOYEE_NOT_FOUND
from src.shared.errors.DuplicateEntryError import DuplicateEntryError
from src.modules.employees.repositories.employees_repository import EmployeesRepository

class UpdateEmployeeUseCase:
    def __init__(self, employees_repository: EmployeesRepository):
        self.employees_repository = employees_repository

    def execute(self, id, data):
        employee = self.employees_repository.get(id)

        if not employee:
            raise AppError(EMPLOYEE_NOT_FOUND, 404)

        data['updated_at'] = timezone.now()
        
        try:
            employee = self.employees_repository.update(employee, data)
            return employee.to_dict()
        except DuplicateEntryError as error:
            raise AppError(error.message, error.statusCode)