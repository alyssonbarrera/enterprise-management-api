from .find_employee_by_criteria_use_case import FindEmployeeByCriteriaUseCase
from src.modules.employees.repositories.employees_repository import EmployeesRepository

def make_find_employee_by_criteria_use_case():
    employees_repository = EmployeesRepository()

    use_case = FindEmployeeByCriteriaUseCase(employees_repository)

    return use_case