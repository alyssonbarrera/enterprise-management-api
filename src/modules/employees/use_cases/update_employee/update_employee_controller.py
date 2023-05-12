from django.http import JsonResponse
from src.utils.validator import validator
from src.utils.uuid_validator import uuid_validator
from django.views.decorators.http import require_http_methods
from ...validators.employee_validation_schema import employee_validation_schema
from src.modules.employees.use_cases.update_employee.make_update_employee_use_case import make_update_employee_use_case

@require_http_methods(['PUT'])
def update_employee_controller(request, id):
    if not id:
        return JsonResponse({'message': 'Id is required'}, status=400)
    
    id = uuid_validator(id)['id']
            
    data = validator(employee_validation_schema, request.json, update=True)

    use_case = make_update_employee_use_case()

    employee = use_case.execute(id, data)

    response = {
        'employee': employee
    }

    return JsonResponse(response, status=200)
    