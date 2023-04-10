from django.urls import path
from src.modules.projects.use_cases.create_project.create_project_controller import create_project_controller

projects_routes = [
    path('create', create_project_controller),
]