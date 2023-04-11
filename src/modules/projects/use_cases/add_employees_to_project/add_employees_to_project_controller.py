from cerberus import Validator
from django.http import JsonResponse
from src.shared.errors.AppError import AppError
from django.views.decorators.http import require_http_methods
from .make_add_employees_to_project_use_case import make_add_employees_to_project_use_case

@require_http_methods(["PATCH"])
def add_employees_to_project_controller(request, id):
    if not id:
        return JsonResponse({"message": "Project id is required"}, status=400)
    
    body_schema = {
        'employees': {
            'type': 'list',
            'required': True,
            'schema': {
                'type': 'string',
                'required': True,
            }
        }
    }

    validator = Validator(body_schema)

    if not validator.validate(request.json):
        return JsonResponse({"message": validator.errors}, status=400)

    try:
        use_case = make_add_employees_to_project_use_case()

        project = use_case.execute(id, request.json.get('employees'))

        response = {
            "project": project,
        }

        return JsonResponse(response, status=200)
    except Exception as error:
        if isinstance(error, AppError):
            return JsonResponse({"message": error.message}, status=error.statusCode)
        return JsonResponse({"message": "Internal server error"}, status=500)