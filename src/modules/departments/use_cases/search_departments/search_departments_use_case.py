from src.modules.departments.repositories.departments_repository import DepartmentsRepository

class SearchDepartmentsUseCase:
    def __init__(self, departments_repository: DepartmentsRepository):
        self.departments_repository = departments_repository

    def execute(self, query):
        return self.departments_repository.search(query)