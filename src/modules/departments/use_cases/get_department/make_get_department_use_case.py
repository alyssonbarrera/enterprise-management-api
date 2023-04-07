from src.modules.departments.repositories.departments_repository import DepartmentsRepository
from src.modules.departments.use_cases.get_department.get_department_use_case import GetDepartmentUseCase

def make_get_department_use_case():
    departments_repository = DepartmentsRepository()
    use_case = GetDepartmentUseCase(departments_repository)

    return use_case
    