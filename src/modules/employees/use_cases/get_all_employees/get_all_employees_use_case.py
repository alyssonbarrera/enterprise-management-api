from ...repositories.employees_repository import EmployeesRepository

class GetAllEmployeesUseCase:
    def __init__(self, employees_repository: EmployeesRepository):
        self.employees_repository = employees_repository

    def execute(self, page=1):
        employees = self.employees_repository.get_all(int(page))

        employees_list = []

        for employee in employees:
            employees_list.append(employee.to_dict())

        return employees_list