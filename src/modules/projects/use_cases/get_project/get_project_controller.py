from django.http import JsonResponse
from src.shared.errors.AppError import AppError
from src.utils.uuid_validator import uuid_validator
from django.views.decorators.http import require_http_methods
from .make_get_project_use_case import make_get_project_use_case
from src.shared.errors.AppValidatorError import AppValidatorError

@require_http_methods(['GET'])
def get_project_controller(request, id):
    try:
        id = uuid_validator(id)['id']

        use_case = make_get_project_use_case()
        project = use_case.execute(id)

        response = {
            'project': project
        }

        return JsonResponse(response, status=200)
    except Exception as error:
        if isinstance(error, AppError) or isinstance(error, AppValidatorError):
            return JsonResponse({'message': error.message}, status=error.statusCode)
        else:
            return JsonResponse({'message': 'Internal server error'}, status=500)