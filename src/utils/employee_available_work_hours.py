from src.shared.errors.AppError import AppError
from src.utils.calculate_metrics import calculate_available_work_hours

def employee_available_work_hours(employee, projects_employees_repository):
    hours_available_by_employee = calculate_available_work_hours(employee, projects_employees_repository)

    if hours_available_by_employee == 0:
        raise AppError(f'Employee {employee.name} has no available work hours', 409)

    return hours_available_by_employee