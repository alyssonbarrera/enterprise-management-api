from django.urls import path
from src.modules.employees.use_cases.create_employee.create_employee_controller import create_employee_controller
from src.modules.employees.use_cases.get_employee.get_employee_controller import get_employee_controller

employees_routes = [
    path('create', create_employee_controller),
    path('get/<str:id>', get_employee_controller),
]