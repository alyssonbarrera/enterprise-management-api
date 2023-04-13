from datetime import datetime
from django.db.utils import IntegrityError
from src.shared.infra.database.models import Employee
from django.core.exceptions import ObjectDoesNotExist
from src.utils.error_messages import EMPLOYEE_DUPLICATE_ENTRY
from src.shared.errors.DuplicateEntryError import DuplicateEntryError

ITEMS_PER_PAGE = 20

class EmployeesRepository:
    def create(self, data):
        date_string = data['birth_date']
        date_obj = datetime.strptime(date_string, '%d/%m/%Y')
        format_date = date_obj.strftime('%Y-%m-%d')

        data['birth_date'] = format_date

        try:
            employee = Employee(**data)
            employee.save()

            return employee
        except IntegrityError:
            raise DuplicateEntryError(EMPLOYEE_DUPLICATE_ENTRY)
    
    def get(self, id):
        try:
            return Employee.objects.get(id=id)
        except ObjectDoesNotExist:
            return None
        
    def find_by_criteria(self, criteria):
        try:
            employee = {}

            for key, value in criteria.items():
                employee = Employee.objects.get(**{key: value})
                
            return employee
        except ObjectDoesNotExist:
            return None

    def get_all(self, page):
        employees = Employee.objects.all()[(page - 1) * ITEMS_PER_PAGE:page * ITEMS_PER_PAGE]

        return list(employees)
    
    def search(self, name, page):
        employees = Employee.objects.filter(name__icontains=name)[(page - 1) * ITEMS_PER_PAGE:page * ITEMS_PER_PAGE]

        return list(employees)

    def update(self, employee, data):
        try:
            for key, value in data.items():
                setattr(employee, key, value)

            employee.save()

            return employee
        except IntegrityError:
            raise DuplicateEntryError(EMPLOYEE_DUPLICATE_ENTRY)
    
    def delete(self, employee):
        return employee.delete()