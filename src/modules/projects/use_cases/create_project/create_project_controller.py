from django.http import JsonResponse
from src.utils.validator import validator
from src.shared.errors.AppError import AppError
from django.views.decorators.http import require_http_methods
from src.shared.errors.AppValidatorError import AppValidatorError
from .make_create_project_use_case import make_create_project_use_case
from ..validators.project_validation_schema import project_validation_schema


@require_http_methods(["POST"])
def create_project_controller(request):
    try:
        data = validator(project_validation_schema, request.json)

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