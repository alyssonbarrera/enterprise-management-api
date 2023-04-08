from src.shared.errors.AppError import AppError
from ...repositories.employees_repository import EmployeesRepository

class GetEmployeeUseCase:
    def __init__(self, employees_repository: EmployeesRepository):
        self.employees_repository = employees_repository

    def execute(self, id):
        employee = self.employees_repository.get(id)

        if not employee:
            raise AppError('Employee not found', 404)
        
        return employee.to_dict()