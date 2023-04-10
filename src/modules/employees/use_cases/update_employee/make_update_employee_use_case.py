from .update_employee_use_case import UpdateEmployeeUseCase
from src.modules.employees.repositories.employees_repository import EmployeesRepository

def make_update_employee_use_case():
    employees_repository = EmployeesRepository()

    use_case = UpdateEmployeeUseCase(employees_repository)

    return use_case