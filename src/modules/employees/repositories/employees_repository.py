from django.db.utils import IntegrityError
from src.shared.infra.database.models import Employee
from django.core.exceptions import ObjectDoesNotExist
from src.shared.errors.DuplicateEntryError import DuplicateEntryError

ITEMS_PER_PAGE = 20

class EmployeesRepository:
    def create(self, data):
        try:
            employee = Employee(**data)
            employee.save()

            return employee
        except IntegrityError:
            raise DuplicateEntryError('Employee already exists')
    
    def get(self, id):
        try:
            return Employee.objects.get(id=id)
        except ObjectDoesNotExist:
            return None

    def get_all(self, page):
        print('CHECK_6 ===========>', page)
        page = int(page)
        employees = Employee.objects.raw(
            f'SELECT * FROM src_employee LIMIT {ITEMS_PER_PAGE} OFFSET {(page - 1) * ITEMS_PER_PAGE}'
        )

        employee_list = list(employees)

        return employee_list
    
    def search(self, name):
        employees = Employee.objects.filter(name__icontains=name).order_by('created_at')

        employees_list = []

        for employee in employees:
            employee_dict = {}

            for key, value in employee.__dict__.items():
                if key != '_state':
                    employee_dict[key] = value

            employees_list.append(employee_dict)

        return employees_list

    def update(self, id, data):
        employee = Employee.objects.get(id=id)
        
        for key, value in data.items():
            setattr(employee, key, value)

        employee.save()

        employee_dict = {}

        for key, value in employee.__dict__.items():
            if key != '_state':
                employee_dict[key] = value

        return employee_dict
    
    def delete(self, id):
        employee = Employee.objects.get(id=id)

        employee.delete()