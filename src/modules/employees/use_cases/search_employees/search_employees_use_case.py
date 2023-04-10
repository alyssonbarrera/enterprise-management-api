from ...repositories.employees_repository import EmployeesRepository

class SearchEmployeesUseCase:
    def __init__(self, employees_repository: EmployeesRepository):
        self.employees_repository = employees_repository

    def execute(self, query, page):
        employees = self.employees_repository.search(query, page)


        employees_list = []

        for employee in employees:
            employees_list.append(employee.to_dict())

        return employees_list