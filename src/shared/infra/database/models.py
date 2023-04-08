import uuid
from django.db import models
from django.core.exceptions import ValidationError

class Department(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    num_projects = models.IntegerField(default=0)
    num_employees = models.IntegerField(default=0)
    updated_at = models.DateTimeField(default=None, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'num_projects': self.num_projects,
            'num_employees': self.num_employees,
            'updated_at': self.updated_at,
            'created_at': self.created_at
        }

    class Meta:
        verbose_name = 'Department'
        verbose_name_plural = 'Departments'
        indexes = [
            models.Index(fields=['name'], name='department_name_index'),
        ]

class Employee(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100, unique=True)
    cpf = models.CharField(max_length=11, unique=True)
    rg = models.CharField(max_length=10, unique=True)
    gender = models.CharField(max_length=20)
    birth_date = models.DateField()
    has_driving_license = models.BooleanField()
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    weekly_workload = models.IntegerField()
    projects = models.ManyToManyField('Project', related_name='employee_projects', through='ProjectEmployee', blank=True)
    department = models.ForeignKey('Department', on_delete=models.CASCADE)
    active = models.BooleanField(default=True)
    updated_at = models.DateTimeField(default=None, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def get_projects(self):
        return [project.to_dict() for project in self.projects.all()]

    def get_department(self):
        return self.department.to_dict() if self.department else None

    def to_dict(self):
        project_ids = list(self.projects.values_list('id', flat=True))
        department = self.department.to_dict() if self.department else None

        return {
            'id': self.id,
            'name': self.name,
            'cpf': self.cpf,
            'rg': self.rg,
            'gender': self.gender,
            'birth_date': self.birth_date,
            'has_driving_license': self.has_driving_license,
            'salary': self.salary,
            'weekly_workload': self.weekly_workload,
            'projects': project_ids,
            'department': department,
            'active': self.active,
            'updated_at': self.updated_at,
            'created_at': self.created_at
        }
    
    class Meta:
        verbose_name = 'Employee'
        verbose_name_plural = 'Employees'
        indexes = [
            models.Index(fields=['name'], name='employee_name_index'),
            models.Index(fields=['cpf'], name='employee_cpf_index'),
            models.Index(fields=['department'], name='employee_department_index'),
        ]

class Project(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    required_hours = models.IntegerField(default=0)
    estimated_deadline = models.DateField(default=None, null=True)
    completed_hours = models.IntegerField(default=0)
    last_hours_calculation_date = models.DateField(default=None, null=True)
    employees = models.ManyToManyField('Employee', related_name='employees_projects', through='ProjectEmployee', blank=True)
    supervisor = models.ForeignKey('Employee', on_delete=models.CASCADE, default=None, null=True)
    department = models.ForeignKey('Department', on_delete=models.CASCADE)
    done = models.BooleanField(default=False)
    updated_at = models.DateTimeField(default=None, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'required_hours': self.required_hours,
            'estimated_deadline': self.estimated_deadline,
            'completed_hours': self.completed_hours,
            'last_hours_calculation_date': self.last_hours_calculation_date,
            'employees': self.employees,
            'supervisor': self.supervisor,
            'department': self.department,
            'done': self.done,
            'updated_at': self.updated_at,
            'created_at': self.created_at
        }

    class Meta:
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'
        indexes = [
            models.Index(fields=['name'], name='project_name_index'),
            models.Index(fields=['supervisor'], name='project_supervisor_index'),
            models.Index(fields=['department'], name='project_department_index'),
            models.Index(fields=['done'], name='project_done_index'),
        ]

    def clean(self):
        if Project.objects.filter(name=self.name, department=self.department).exists():
            raise ValidationError("Project already exists in this department")

class ProjectEmployee(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    project = models.ForeignKey('Project', on_delete=models.CASCADE)
    employee = models.ForeignKey('Employee', on_delete=models.CASCADE)
    employee_workload = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def to_dict(self):
        return {
            'id': self.id,
            'project': self.project,
            'employee': self.employee,
            'employee_workload': self.employee_workload,
            'created_at': self.created_at
        }
    
    class Meta:
        verbose_name = 'ProjectEmployee'
        verbose_name_plural = 'ProjectsEmployees'
