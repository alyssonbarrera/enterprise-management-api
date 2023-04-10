from src.shared.infra.database.models import Department
from django.core.exceptions import ObjectDoesNotExist

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
        departments = Department.objects.raw(
            f'SELECT * FROM src_department LIMIT {ITEMS_PER_PAGE} OFFSET {(page - 1) * ITEMS_PER_PAGE}'
        )

        departments_list = list(departments)

        return departments_list

    def search(self, name, page):
        departments = Department.objects.raw(
            f'SELECT * FROM src_department WHERE name LIKE "%{name}%" LIMIT {ITEMS_PER_PAGE} OFFSET {(page - 1) * ITEMS_PER_PAGE}'
        )

        departments_list = list(departments)

        return departments_list
    
    def has_active_employees(self, id):
        department = Department.objects.get(id=id)

        return department.has_active_employees()
    
    def has_active_projects(self, id):
        department = Department.objects.get(id=id)

        return department.has_active_projects()

    def get_by_name(self, name):
        department = Department.objects.filter(name=name)
        
        return department
    
    def update(self, id, data):
        department = Department.objects.get(id=id)
        
        for key, value in data.items():
            setattr(department, key, value)

        department.save()

        return department
    
    def delete(self, department):        
        return department.delete()