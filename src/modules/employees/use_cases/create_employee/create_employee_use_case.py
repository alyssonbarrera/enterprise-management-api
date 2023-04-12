from src.shared.errors.AppError import AppError
from src.utils.error_messages import DEPARTMENT_NOT_FOUND
from ...repositories.employees_repository import EmployeesRepository
from src.shared.errors.DuplicateEntryError import DuplicateEntryError
from ....departments.repositories.departments_repository import DepartmentsRepository

class CreateEmployeeUseCase:
    def __init__(
            self,
            employees_repository: EmployeesRepository,
            departments_repository: DepartmentsRepository
        ):
        self.employees_repository = employees_repository
        self.departments_repository = departments_repository

    def execute(self, data):
        try:
            department = self.departments_repository.get(data['department'])

            if not department:
                raise AppError(DEPARTMENT_NOT_FOUND, 404)
            
            data['department'] = department

            employee = self.employees_repository.create(data)

            return employee.to_dict()
        except DuplicateEntryError as error:
            raise AppError(error.message, error.statusCode)