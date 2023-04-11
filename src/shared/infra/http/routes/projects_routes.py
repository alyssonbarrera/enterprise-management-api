from django.urls import path
from src.modules.projects.use_cases.create_project.create_project_controller import create_project_controller
from src.modules.projects.use_cases.delete_project.delete_project_controller import delete_project_controller
from src.modules.projects.use_cases.update_project.update_project_controller import update_project_controller
from src.modules.projects.use_cases.search_projects.search_projects_controller import search_projects_controller
from src.modules.projects.use_cases.get_all_projects.get_all_projects_controller import get_all_projects_controller
from src.modules.projects.use_cases.fetch_project_metrics.fetch_project_metrics_controller import fetch_project_metrics_controller
from src.modules.projects.use_cases.find_project_by_criteria.find_project_by_criteria_controller import find_project_by_criteria_controller
from src.modules.projects.use_cases.add_employees_to_project.add_employees_to_project_controller import add_employees_to_project_controller
from src.modules.projects.use_cases.remove_employees_to_project.remove_employees_to_project_controller import remove_employees_to_project_controller

projects_routes = [
    path('create', create_project_controller),
    path('get', find_project_by_criteria_controller),
    path('get/all', get_all_projects_controller),
    path('search', search_projects_controller),
    path('delete/<str:id>', delete_project_controller),
    path('update/<str:id>', update_project_controller),
    path('add/employees/<str:id>', add_employees_to_project_controller),
    path('remove/employees/<str:id>', remove_employees_to_project_controller),
    path('metrics/<str:id>', fetch_project_metrics_controller),
]