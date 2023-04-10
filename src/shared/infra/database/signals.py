from django.dispatch import receiver
from django.db.models.signals import pre_delete
from django.db.models.signals import post_save, post_delete
from src.shared.infra.database.models import Employee, Project, ProjectEmployee
from django.db.models import Sum

@receiver(post_save, sender=Project)
@receiver(post_delete, sender=Project)
def update_department_projects(sender, instance, **kwargs):
    department = instance.department
    department.num_projects = Project.objects.filter(department=department).count()
    department.save()

@receiver(post_save, sender=Employee)
@receiver(post_delete, sender=Employee)
def update_department_employees(sender, instance, **kwargs):
    department = instance.department
    department.num_employees = Employee.objects.filter(department=department).count()
    department.save()

@receiver(post_save, sender=Employee)
def update_department_employee_move(sender, instance, **kwargs):
    old_department = instance.department
    new_department = instance.department
    if old_department != new_department:
        old_department.num_employees = Employee.objects.filter(department=old_department).count()
        old_department.save()
        new_department.num_employees = Employee.objects.filter(department=new_department).count()
        new_department.save()

@receiver(post_save, sender=Project)
def update_department_project_move(sender, instance, **kwargs):
    old_department = instance.department
    new_department = instance.department
    if old_department != new_department:
        old_department.num_projects = Project.objects.filter(department=old_department).count()
        old_department.save()
        new_department.num_projects = Project.objects.filter(department=new_department).count()
        new_department.save()

@receiver(pre_delete, sender=Employee)
def remove_project_employee(sender, instance, **kwargs):
    instance.projects.through.objects.filter(employee_id=instance.id).delete()