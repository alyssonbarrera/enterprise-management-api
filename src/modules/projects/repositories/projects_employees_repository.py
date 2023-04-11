from django.db import connection
from django.db.models import Sum
from src.shared.infra.database.models import Project, ProjectEmployee

class ProjectsEmployeesRepository:
    def add_employee_to_project(self, project, employee_data):
        project.employees.add(
            employee_data['employee'],
            through_defaults={'hours_worked_per_week': employee_data['hours_worked_per_week']}
        )

    def add_supervisor_to_project(self, project, supervisor_data):
        project.employees.add(
            supervisor_data['supervisor'],
            through_defaults={'hours_worked_per_week': supervisor_data['hours_worked_per_week'], 'role': 'supervisor'}
        )

    def delete(self, project):
        ProjectEmployee.objects.filter(project=project).delete()

    def remove_employee_from_project(self, project, employee):
        project.employees.remove(employee)

    def delete_employees_from_project(self, project):
        project_employees = project.employees.filter(projectemployee__role='employee')

        if project_employees:
            project.employees.remove(*project_employees)

    def replace_supervisor_in_project(self, project, supervisor):
        project_supervisor = project.projectemployee_set.filter(role='supervisor').first()

        if project_supervisor:
            project.employees.remove(project_supervisor.employee)

        project.employees.add(
            supervisor['supervisor'],
            through_defaults={'hours_worked_per_week': supervisor['hours_worked_per_week'], 'role': 'supervisor'}
        )

    def get_by_project(self, project_id):
        data = ProjectEmployee.objects.filter(project=project_id).values('employee', 'hours_worked_per_week', 'role')

        return list(data)
    
    def get_all(self):
        data = ProjectEmployee.objects.all().values('project', 'employee', 'hours_worked_per_week', 'role')

        return list(data)

    def calculate_hours_worked(self, employee):
        projects = Project.objects.filter(employees__id=employee['id'])
        hours_worked_per_project = []
    
        for project in projects:
            project_employee = ProjectEmployee.objects.get(project=project, employee=employee)
            hours_worked = project_employee['hours_worked_per_week'] - project['completed_hours']
            hours_worked_per_project.append(hours_worked)

        total_hours_worked = sum(hours_worked_per_project)

        return total_hours_worked

    def get_hours_worked_per_week(self, employee):
        hours_worked_per_week = ProjectEmployee.objects.filter(employee=employee).aggregate(Sum('hours_worked_per_week'))['hours_worked_per_week__sum'] or 0

        return hours_worked_per_week