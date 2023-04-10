from src.shared.errors.AppError import AppError
from src.utils.error_messages import EMPLOYEE_NOT_FOUND
from ...repositories.employees_repository import EmployeesRepository

class FindEmployeeByCriteriaUseCase:
    def __init__(self, employees_repository: EmployeesRepository):
        self.employees_repository = employees_repository

    def execute(self, criteria):
        employee = self.employees_repository.find_by_criteria(criteria)

        if not employee:
            raise AppError(EMPLOYEE_NOT_FOUND, 404)
        
        return employee.to_dict()