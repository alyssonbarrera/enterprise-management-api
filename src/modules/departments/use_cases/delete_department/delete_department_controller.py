from src.shared.errors.AppError import AppError
from django.http import HttpResponse, JsonResponse
from src.utils.uuid_validator import uuid_validator
from django.views.decorators.http import require_http_methods
from src.shared.errors.AppValidatorError import AppValidatorError
from src.modules.departments.use_cases.delete_department.make_delete_department_use_case import make_delete_department_use_case

@require_http_methods(['DELETE'])
def delete_department_controller(request, id):
    try:
        if not id:
            return JsonResponse({'message': 'Id is required'}, status=400)
        
        id = uuid_validator(id)['id']
        
        use_case = make_delete_department_use_case()
        use_case.execute(id)

        return HttpResponse(status=204)
    except Exception as error:
        if isinstance(error, AppError) or isinstance(error, AppValidatorError):
            return JsonResponse({'message': error.message}, status=error.statusCode)
        return JsonResponse({'message': 'Internal server error'}, status=500)