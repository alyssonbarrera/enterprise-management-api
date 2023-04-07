from src.modules.departments.repositories.departments_repository import DepartmentsRepository
from src.modules.departments.use_cases.search_departments.search_departments_use_case import SearchDepartmentsUseCase

def make_search_departments_use_case():
    departments_repository = DepartmentsRepository()
    use_case = SearchDepartmentsUseCase(departments_repository)

    return use_case
