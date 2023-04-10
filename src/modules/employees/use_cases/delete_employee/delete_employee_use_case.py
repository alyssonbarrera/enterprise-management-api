from src.shared.errors.AppError import AppError
from src.utils.error_messages import EMPLOYEE_NOT_FOUND
from src.modules.employees.repositories.employees_repository import EmployeesRepository

class DeleteEmployeeUseCase:
    def __init__(self, employees_repository: EmployeesRepository):
        self.employees_repository = employees_repository

    def execute(self, id):
        employee = self.employees_repository.get(id)

        if not employee:
            raise AppError(EMPLOYEE_NOT_FOUND, 404)
        
        self.employees_repository.delete(employee)