from src.modules.departments.repositories.departments_repository import DepartmentsRepository

class SearchDepartmentsUseCase:
    def __init__(self, departments_repository: DepartmentsRepository):
        self.departments_repository = departments_repository

    def execute(self, query, page):
        employees = self.departments_repository.search(query, page)

        employees_list = []

        for employee in employees:
            employees_list.append(employee.to_dict())

        return employees_list