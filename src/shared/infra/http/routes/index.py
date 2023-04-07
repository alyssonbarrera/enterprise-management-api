from django.urls import path
from src.shared.infra.http.routes.departments_routes import departmentsRoutes
from django.urls import include

urlpatterns = [
    path('departments/', include(departmentsRoutes())),
]
