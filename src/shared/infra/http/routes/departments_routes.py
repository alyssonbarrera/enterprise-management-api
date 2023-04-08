from django.urls import path
from src.modules.departments.use_cases.get_department.get_department_controller import get_department_controller
from src.modules.departments.use_cases.create_department.create_department_controller import create_department_controller
from src.modules.departments.use_cases.delete_department.delete_department_controller import delete_department_controller
from src.modules.departments.use_cases.update_department.update_department_controller import update_department_controller
from src.modules.departments.use_cases.search_departments.search_departments_controller import search_departments_controller
from src.modules.departments.use_cases.get_all_departments.get_all_departments_controller import get_all_departments_controller

departments_routes = [
    path('create', create_department_controller),
    path('get/all', get_all_departments_controller),
    path('get/<str:id>', get_department_controller),
    path('search', search_departments_controller),
    path('delete/<str:id>', delete_department_controller),
    path('update/<str:id>', update_department_controller)
]