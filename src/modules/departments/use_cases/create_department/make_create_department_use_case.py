from src.modules.departments.repositories.departments_repository import DepartmentsRepository
from src.modules.departments.use_cases.create_department.create_department_use_case import CreateDepartmentUseCase

def make_create_department_use_case():
    departments_repository = DepartmentsRepository()
    use_case = CreateDepartmentUseCase(departments_repository)

    return use_case
    