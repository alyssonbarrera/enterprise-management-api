from django.http import JsonResponse
from src.utils.validator import validator
from src.utils.uuid_validator import uuid_validator
from django.views.decorators.http import require_http_methods
from ...validators.department_validation_schema import department_validation_schema
from src.modules.departments.use_cases.update_department.make_update_department_use_case import make_update_department_use_case

@require_http_methods(['PUT'])
def update_department_controller(request, id):
    if not id:
        return JsonResponse({'message': 'Id is required'}, status=400)
    
    id = uuid_validator(id)['id']
    
    data = validator(department_validation_schema, request.json, update=True)

    use_case = make_update_department_use_case()

    department = use_case.execute(id, data)

    response = {
        'department': department
    }

    return JsonResponse(response, status=200)
