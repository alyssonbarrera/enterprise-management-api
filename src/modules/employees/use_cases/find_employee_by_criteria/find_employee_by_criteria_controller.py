from django.http import JsonResponse
from src.utils.validator import validator
from src.shared.errors.AppError import AppError
from django.views.decorators.http import require_http_methods
from src.shared.errors.AppValidatorError import AppValidatorError
from .make_find_employee_by_criteria_use_case import make_find_employee_by_criteria_use_case
from ...validators.find_employee_by_criteria_query_schema import find_employee_by_criteria_query_schema

@require_http_methods(['GET'])
def find_employee_by_criteria_controller(request):
    try:
        query = validator(find_employee_by_criteria_query_schema, request.GET)

        use_case = make_find_employee_by_criteria_use_case()
        employee = use_case.execute(query)

        response = {
            'employee': employee
        }

        return JsonResponse(response, status=200)
    except Exception as error:
        if isinstance(error, AppError) or isinstance(error, AppValidatorError):
            return JsonResponse({'message': error.message}, status=error.statusCode)
        else:
            return JsonResponse({'message': 'Internal server error'}, status=500)
    