from django.http import JsonResponse
from src.utils.uuid_validator import uuid_validator
from django.views.decorators.http import require_http_methods
from .make_get_project_use_case import make_get_project_use_case

@require_http_methods(['GET'])
def get_project_controller(request, id):
    id = uuid_validator(id)['id']

    use_case = make_get_project_use_case()

    project = use_case.execute(id)

    response = {
        'project': project
    }

    return JsonResponse(response, status=200)
