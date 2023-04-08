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
        page = int(page)
        departments = Department.objects.raw(
            f'SELECT * FROM src_department LIMIT {ITEMS_PER_PAGE} OFFSET {(page - 1) * ITEMS_PER_PAGE}'
        )

        department_list = list(departments)

        return department_list

    def search(self, name):
        departments = Department.objects.filter(name__icontains=name).order_by('created_at')

        departments_list = []

        for department in departments:
            department_dict = {}

            for key, value in department.__dict__.items():
                if key != '_state':
                    department_dict[key] = value

            departments_list.append(department_dict)

        return departments_list
    
    def get_by_name(self, name):
        department = Department.objects.filter(name=name)
        
        return department
    
    def update(self, id, data):
        department = Department.objects.get(id=id)
        
        for key, value in data.items():
            setattr(department, key, value)

        department.save()

        department_dict = {}

        for key, value in department.__dict__.items():
            if key != '_state':
                department_dict[key] = value

        return department_dict
    
    def delete(self, id):
        department = Department.objects.get(id=id)
        
        department.delete()