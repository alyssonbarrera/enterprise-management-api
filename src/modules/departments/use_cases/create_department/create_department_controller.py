from django.http import JsonResponse
from src.utils.validator import validator
from django.views.decorators.http import require_http_methods
from ...validators.department_validation_schema import department_validation_schema
from src.modules.departments.use_cases.create_department.make_create_department_use_case import make_create_department_use_case

@require_http_methods(['POST'])
def create_department_controller(request):
    data = validator(department_validation_schema, request.json)

    use_case = make_create_department_use_case()

    department = use_case.execute(data)

    response = {
        'department': department,
    }

    return JsonResponse(response, status=201)
