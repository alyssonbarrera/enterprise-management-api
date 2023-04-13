from django.http import JsonResponse
from src.utils.validator import validator
from src.shared.errors.AppError import AppError
from django.views.decorators.http import require_http_methods
from src.shared.errors.AppValidatorError import AppValidatorError
from .make_create_project_use_case import make_create_project_use_case
from ...validators.project_validation_schema import project_validation_schema
from src.modules.projects.validators.supervisor_body_schema import supervisor_body_schema
from src.modules.projects.validators.add_and_remove_employees_body_schema import add_and_remove_employees_body_schema

@require_http_methods(["POST"])
def create_project_controller(request):
    try:
        data = validator(project_validation_schema, request.json)

        if "employees" in data:
            data_employees = validator(add_and_remove_employees_body_schema, {'employees': data["employees"]}, variant="list_employees")
            data["employees"] = data_employees.get("employees")

        if 'supervisor' in data:
            data_supervisor = validator(supervisor_body_schema, {'supervisor': data["supervisor"]}, variant="supervisor")
            data["supervisor"] = data_supervisor.get("supervisor")

        use_case = make_create_project_use_case()

        project = use_case.execute(data)

        response = {
            "project": project,
        }

        return JsonResponse(response, status=201)
    except Exception as error:
        if isinstance(error, AppError) or isinstance(error, AppValidatorError):
            return JsonResponse({"message": error.message}, status=error.statusCode)
        return JsonResponse({"message": "Internal server error"}, status=500)