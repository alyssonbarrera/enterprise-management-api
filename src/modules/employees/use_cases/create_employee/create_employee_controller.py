from django.http import JsonResponse
from src.utils.validator import validator
from django.views.decorators.http import require_http_methods
from .make_create_employee_use_case import make_create_employee_use_case
from ...validators.employee_validation_schema import employee_validation_schema

@require_http_methods(['POST'])
def create_employee_controller(request):
    data = validator(employee_validation_schema, request.json)

    use_case = make_create_employee_use_case()

    employee = use_case.execute(data)

    response = {
        'employee': employee
    }

    return JsonResponse(response, status=201)
