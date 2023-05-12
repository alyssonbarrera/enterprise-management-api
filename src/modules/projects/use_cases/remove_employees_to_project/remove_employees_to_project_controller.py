from django.http import JsonResponse
from src.utils.validator import validator
from src.utils.uuid_validator import uuid_validator
from django.views.decorators.http import require_http_methods
from ...validators.add_and_remove_employees_body_schema import add_and_remove_employees_body_schema
from .make_remove_employees_to_project_use_case import make_remove_employees_to_project_use_case

@require_http_methods(["PATCH"])
def remove_employees_to_project_controller(request, id):
    if not id:
        return JsonResponse({"message": "Project id is required"}, status=400)
    
    id = uuid_validator(id)['id']

    data = validator(add_and_remove_employees_body_schema, request.json, variant='list_employees')

    use_case = make_remove_employees_to_project_use_case()

    project = use_case.execute(id, data['employees'])

    response = {
        "project": project,
    }

    return JsonResponse(response, status=200)
