from django.http import JsonResponse
from src.utils.validator import validator
from django.views.decorators.http import require_http_methods
from .make_find_employee_by_criteria_use_case import make_find_employee_by_criteria_use_case
from ...validators.find_employee_by_criteria_query_schema import find_employee_by_criteria_query_schema

@require_http_methods(['GET'])
def find_employee_by_criteria_controller(request):
    query = validator(find_employee_by_criteria_query_schema, request.GET)

    use_case = make_find_employee_by_criteria_use_case()

    employee = use_case.execute(query)

    response = {
        'employee': employee
    }

    return JsonResponse(response, status=200)
