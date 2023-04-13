from django.http import JsonResponse
from src.utils.validator import validator
from src.shared.errors.AppError import AppError
from src.utils.uuid_validator import uuid_validator
from django.views.decorators.http import require_http_methods
from src.shared.errors.AppValidatorError import AppValidatorError
from ...validators.project_validation_schema import project_validation_schema
from src.modules.projects.use_cases.update_project.make_update_project_use_case import make_update_project_use_case

@require_http_methods(['PUT'])
def update_project_controller(request, id):
    try:
        if not id:
            return JsonResponse({'message': 'Id is required'}, status=400)
        
        id = uuid_validator(id)['id']
        
        data = validator(project_validation_schema, request.json, update=True)

        use_case = make_update_project_use_case()

        project = use_case.execute(id, data)

        response = {
            'project': project
        }

        return JsonResponse(response, status=200)
    except Exception as error:
        if isinstance(error, AppError) or isinstance(error, AppValidatorError):
            return JsonResponse({'message': error.message}, status=error.statusCode)
        return JsonResponse({'message': 'Internal server error'}, status=500)