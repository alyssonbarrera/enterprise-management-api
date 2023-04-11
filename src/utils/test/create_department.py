from src.modules.departments.repositories.departments_repository import DepartmentsRepository

def create_department(number=1):
    departments_repository = DepartmentsRepository()

    department_data = {
        'name': f'Department Test {number}',
        'description': 'Department Test Description',
    }

    department = departments_repository.create(department_data)
    
    return {
        'department': department.to_dict(),
        'Department': department,
    }