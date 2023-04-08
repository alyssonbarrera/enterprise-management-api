from django.urls import path
from django.urls import include
from .departments_routes import departments_routes
from .employees_routes import employees_routes

urlpatterns = [
    path('departments/', include(departments_routes)),
    path('employees/', include(employees_routes)),
]
