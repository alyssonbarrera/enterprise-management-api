from django.core.exceptions import ObjectDoesNotExist
from src.shared.infra.database.models import Department

ITEMS_PER_PAGE = 20

class DepartmentsRepository:
    def create(self, data):
        department = Department(**data)
        department.save()

        return department
    
    def get(self, id):
        try:
            return Department.objects.get(id=id)
        except ObjectDoesNotExist:
            return None

    def get_all(self, page):
        departments = Department.objects.all()[(page - 1) * ITEMS_PER_PAGE:page * ITEMS_PER_PAGE]

        return list(departments)

    def search(self, name, page):
        departments = Department.objects.filter(name__icontains=name)[(page - 1) * ITEMS_PER_PAGE:page * ITEMS_PER_PAGE]

        return list(departments)
    
    def has_active_employees(self, id):
        department = Department.objects.get(id=id)

        return department.has_active_employees()
    
    def has_active_projects(self, id):
        department = Department.objects.get(id=id)

        return department.has_active_projects()

    def get_by_name(self, name):
        department = Department.objects.filter(name=name)
        
        return department
    
    def update(self, department, data):     
        for key, value in data.items():
            setattr(department, key, value)

        department.save()

        return department
    
    def delete(self, department):        
        return department.delete()