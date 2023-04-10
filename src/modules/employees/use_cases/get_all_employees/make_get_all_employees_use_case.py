from .get_all_employees_use_case import GetAllEmployeesUseCase
from ...repositories.employees_repository import EmployeesRepository

def make_get_all_employees_use_case():
    employees_repository = EmployeesRepository()

    use_case = GetAllEmployeesUseCase(employees_repository)

    return use_case