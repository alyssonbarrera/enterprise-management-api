from datetime import datetime
from django.utils.timezone import make_aware

def calculate_remaining_hours(project):
    total_hours_worked = project.completed_hours
    start_date = project.start_date

    estimated_deadline = project.estimated_deadline

    if project.end_date or start_date > estimated_deadline:
        return 0

    hours_until_project_completion = (estimated_deadline - start_date).total_seconds() / (60 * 60)

    remaining_hours = round(hours_until_project_completion - total_hours_worked)

    return max(0, remaining_hours)

def calculate_available_work_hours(employee, projects_employees_repository):
    hours_worked = projects_employees_repository.get_hours_worked_per_week(employee)
    weekly_workload = employee.weekly_workload
    hours_available = weekly_workload - hours_worked

    return hours_available

def calculate_and_update_project_hours(project):
    now = datetime.now()

    if not isinstance(project.estimated_deadline, datetime):
        project.estimated_deadline = datetime.strptime(str(project.estimated_deadline), '%Y-%m-%d')

    if project.start_date and not isinstance(project.start_date, datetime):
        project.start_date = datetime.strptime(str(project.start_date), '%Y-%m-%d')

    if project.end_date and not isinstance(project.end_date, datetime):
        project.end_date = datetime.strptime(str(project.end_date), '%Y-%m-%d')

    if project.last_hours_calculation_date and not isinstance(project.last_hours_calculation_date, datetime):
        project.last_hours_calculation_date = datetime.strptime(str(project.last_hours_calculation_date), '%Y-%m-%d')

    estimated_deadline = project.estimated_deadline
    start_date = project.start_date if project.start_date is not None else now
    end_date = project.end_date
    final_date = end_date if end_date is not None else estimated_deadline

    project.start_date = start_date
    project.end_date = end_date
    project.final_date = final_date

    last_calculation_date = project.last_hours_calculation_date

    weeks_since_last_calculation = calculate_weeks_since_last_calculation(last_calculation_date, start_date, final_date)

    project_employees = project.projectemployee_set.all()

    total_hours = calculate_employee_total_hours_worked(project_employees, weeks_since_last_calculation, start_date, final_date, project)
    
    project.completed_hours = 0 if not end_date else total_hours
    project.last_hours_calculation_date = now

    project.remaining_hours = calculate_remaining_hours(project)

    if end_date is not None:
        project.done = True
        project.remaining_hours = 0

    project.save()

    return total_hours

def calculate_weeks_since_last_calculation(last_calculation_date, start_date, final_date):
    now = datetime.now()
    if last_calculation_date is None:
        last_calculation_date = start_date

    if last_calculation_date > final_date:
        return (final_date - start_date).total_seconds() / (60 * 60 * 24 * 7)
    elif last_calculation_date < final_date:
        return (final_date - last_calculation_date).total_seconds() / (60 * 60 * 24 * 7)
    else:
        return (now - last_calculation_date).total_seconds() / (60 * 60 * 24 * 7)
    
def calculate_employee_total_hours_worked(project_employees, weeks_since_last_calculation, start_date, final_date, project):
    total_hours = 0
    employees_total_hours_worked = 0

    for project_employee in project_employees:
        hours_worked_per_week = project_employee.hours_worked_per_week
        employees_total_hours_worked += hours_worked_per_week

    if weeks_since_last_calculation < 1:
        total_hours = (employees_total_hours_worked / 5) * (final_date - start_date).total_seconds() / (60 * 60 * 24)
    else:
        total_hours = employees_total_hours_worked * weeks_since_last_calculation

    if employees_total_hours_worked > 0:
        total_hours += project.completed_hours

    return round(total_hours) if total_hours > 1 else 0