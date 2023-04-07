from src.modules.departments.repositories.departments_repository import DepartmentsRepository
from src.modules.departments.use_cases.get_all_departments.get_all_departments_use_case import GetAllDepartmentsUseCase

def make_get_all_departments_use_case():
    departments_repository = DepartmentsRepository()
    use_case = GetAllDepartmentsUseCase(departments_repository)

    return use_case
