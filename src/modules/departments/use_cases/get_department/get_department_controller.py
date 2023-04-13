from django.http import JsonResponse
from src.shared.errors.AppError import AppError
from src.utils.uuid_validator import uuid_validator
from django.views.decorators.http import require_http_methods
from src.shared.errors.AppValidatorError import AppValidatorError
from src.modules.departments.use_cases.get_department.make_get_department_use_case import make_get_department_use_case

@require_http_methods(['GET'])
def get_department_controller(request, id):
    try:
        if not id:
            return JsonResponse({'message': 'Id is required'}, status=400)
        
        id = uuid_validator(id)['id']
        
        use_case = make_get_department_use_case()
        department = use_case.execute(id)

        response = {
            'department': department,
        }

        return JsonResponse(response, status=200)
    
    except Exception as error:
        if isinstance(error, AppError) or isinstance(error, AppValidatorError):
            return JsonResponse({'message': error.message}, status=error.statusCode)
        else:
            return JsonResponse({'message': 'Internal server error'}, status=500)