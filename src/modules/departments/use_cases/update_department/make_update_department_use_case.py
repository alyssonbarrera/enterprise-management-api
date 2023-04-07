from src.modules.departments.repositories.departments_repository import DepartmentsRepository
from src.modules.departments.use_cases.update_department.update_department_use_case import UpdateDepartmentUseCase

def make_update_department_use_case():
    departments_repository = DepartmentsRepository()
    use_case = UpdateDepartmentUseCase(departments_repository)

    return use_case
