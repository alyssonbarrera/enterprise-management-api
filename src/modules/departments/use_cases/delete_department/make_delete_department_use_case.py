from src.modules.departments.repositories.departments_repository import DepartmentsRepository
from src.modules.departments.use_cases.delete_department.delete_department_use_case import DeleteDepartmentUseCase

def make_delete_department_use_case():
    departments_repository = DepartmentsRepository()
    use_case = DeleteDepartmentUseCase(departments_repository)

    return use_case
