from django.urls import path
from src.modules.employees.use_cases.find_employee_by_criteria.find_employee_by_criteria_controller import find_employee_by_criteria_controller
from src.modules.employees.use_cases.create_employee.create_employee_controller import create_employee_controller
from src.modules.employees.use_cases.update_employee.update_employee_controller import update_employee_controller
from src.modules.employees.use_cases.search_employees.search_employees_controller import search_employees_controller
from src.modules.employees.use_cases.get_all_employees.get_all_employees_controller import get_all_employees_controller
from src.modules.employees.use_cases.delete_employee.delete_employee_controller import delete_employee_controller

employees_routes = [
    path('create', create_employee_controller),
    path('get/all', get_all_employees_controller),
    path('get', find_employee_by_criteria_controller),
    path('search', search_employees_controller),
    path('update/<str:id>', update_employee_controller),
    path('delete/<str:id>', delete_employee_controller),
]