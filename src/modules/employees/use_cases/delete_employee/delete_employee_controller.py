from django.http import HttpResponse, JsonResponse
from src.utils.uuid_validator import uuid_validator
from django.views.decorators.http import require_http_methods
from src.modules.employees.use_cases.delete_employee.make_delete_employee_use_case import make_delete_employee_use_case

@require_http_methods(['DELETE'])
def delete_employee_controller(request, id):
    if not id:
        return JsonResponse({'message': 'Id is required'}, status=400)
    
    id = uuid_validator(id)['id']

    use_case = make_delete_employee_use_case()

    use_case.execute(id)

    return HttpResponse(status=204)
