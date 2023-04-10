from src.modules.departments.repositories.departments_repository import DepartmentsRepository

class GetAllDepartmentsUseCase:
    def __init__(self, departments_repository: DepartmentsRepository):
        self.departments_repository = departments_repository

    def execute(self, page=1):
        departments = self.departments_repository.get_all(page)

        departments_list = []

        for department in departments:
            departments_list.append(department.to_dict())
                
        return departments_list