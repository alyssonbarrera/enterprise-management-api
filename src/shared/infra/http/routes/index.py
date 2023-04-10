from django.urls import path
from django.urls import include
from .projects_routes import projects_routes
from .employees_routes import employees_routes
from .departments_routes import departments_routes

urlpatterns = [
    path('departments/', include(departments_routes)),
    path('employees/', include(employees_routes)),
    path('projects/', include(projects_routes)),
]
