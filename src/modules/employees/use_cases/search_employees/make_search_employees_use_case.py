from .search_employees_use_case import SearchEmployeesUseCase
from src.modules.employees.repositories.employees_repository import EmployeesRepository

def make_search_employees_use_case():
    employees_repository = EmployeesRepository()

    use_case = SearchEmployeesUseCase(employees_repository)

    return use_case