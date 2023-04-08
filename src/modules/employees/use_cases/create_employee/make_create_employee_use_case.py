from .create_employee_use_case import CreateEmployeeUseCase
from ...repositories.employees_repository import EmployeesRepository
from ....departments.repositories.departments_repository import DepartmentsRepository

def make_create_employee_use_case():
    employees_repository = EmployeesRepository()
    departments_repository = DepartmentsRepository()

    use_case = CreateEmployeeUseCase(
        employees_repository,
        departments_repository
    )

    return use_case