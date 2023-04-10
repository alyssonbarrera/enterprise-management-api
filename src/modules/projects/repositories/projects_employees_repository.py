from django.db.models import Sum
from src.shared.infra.database.models import Project, ProjectEmployee

class ProjectsEmployeesRepository:
    def add_employees_to_project(self, project, employees):
        for employee in employees:
            project.employees.add(
                employee['employee'],
                through_defaults={'hours_worked_per_week': employee['hours_worked_per_week']}
            )

    def add_supervisor_to_project(self, project, supervisor):
        project.employees.add(
            supervisor['supervisor'],
            through_defaults={'hours_worked_per_week': supervisor['hours_worked_per_week'], 'role': 'supervisor'}
        )

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