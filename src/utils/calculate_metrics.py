from datetime import datetime

def calculate_remaining_hours(project):
    total_hours_worked = project['completed_hours']
    
    estimated_deadline = project['estimated_deadline']
    initial_date = project['start_date'] if 'start_date' in project else datetime.now()

    hours_until_project_completion = (estimated_deadline - initial_date).days * 24

    remaining_hours = hours_until_project_completion - total_hours_worked

    return max(0, remaining_hours)

def calculate_completed_hours(project):
    last_calculation_date = project['last_hours_calculation_date']

    if not last_calculation_date:
        return 0

    time_since_last_calculation = datetime.now() - last_calculation_date
    hours_since_last_calculation = time_since_last_calculation.days * 24

    return project['completed_hours'] + hours_since_last_calculation

def calculate_employee_workload(total_hours_worked, employees):
    num_employees = len(employees)
    if num_employees == 0:
        return {}

    employee_workload = {}
    workload_per_employee = total_hours_worked / num_employees

    for employee in employees:
        employee_workload[employee.id] = workload_per_employee * employee['weekly_workload'] / 40

    return employee_workload

def calculate_available_work_hours(employee, projects_employees_repository):
    hours_worked = projects_employees_repository.get_hours_worked_per_week(employee)
    weekly_workload = employee.weekly_workload
    hours_available = weekly_workload - hours_worked

    return hours_available

def calculate_project_hours(project):
    now = datetime.now()

    last_calculation_date = project.last_hours_calculation_date
    weeks_since_last_calculation = (now - last_calculation_date).total_seconds() / (7 * 24 * 60 * 60)

    total_hours = 0

    project_employees = project.projectemployee_set.all()

    for project_employee in project_employees:
        hours_worked_per_week = project_employee.hours_worked_per_week

        total_hours += hours_worked_per_week * weeks_since_last_calculation

    project.completed_hours = round(total_hours)
    project.last_hours_calculation_date = now

    if project.end_date and project.end_date < now:
        project.done = True
        project.remaining_hours = 0

    project.save()

    return round(total_hours)