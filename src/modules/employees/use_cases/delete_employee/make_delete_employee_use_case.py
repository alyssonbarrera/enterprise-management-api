from .delete_employee_use_case import DeleteEmployeeUseCase
from ...repositories.employees_repository import EmployeesRepository

def make_delete_employee_use_case():
    employees_repository = EmployeesRepository()
    use_case = DeleteEmployeeUseCase(employees_repository)

    return use_case