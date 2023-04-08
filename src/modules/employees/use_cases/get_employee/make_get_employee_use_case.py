from .get_employee_use_case import GetEmployeeUseCase
from src.modules.employees.repositories.employees_repository import EmployeesRepository

def make_get_employee_use_case():
    employees_repository = EmployeesRepository()

    use_case = GetEmployeeUseCase(employees_repository)

    return use_case