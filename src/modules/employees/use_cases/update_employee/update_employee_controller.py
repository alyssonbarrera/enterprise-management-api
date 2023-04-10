from django.http import JsonResponse
from src.utils.validator import validator
from src.shared.errors.AppError import AppError
from django.views.decorators.http import require_http_methods
from src.shared.errors.AppValidatorError import AppValidatorError
from ...validators.employee_validation_schema import employee_validation_schema
from src.modules.employees.use_cases.update_employee.make_update_employee_use_case import make_update_employee_use_case

@require_http_methods(['PUT'])
def update_employee_controller(request, id):
    try:
        if not id:
            return JsonResponse({'message': 'Id is required'}, status=400)
                
        data = validator(employee_validation_schema, request.json, update=True)

        use_case = make_update_employee_use_case()

        employee = use_case.execute(id, data)

        response = {
            'employee': employee
        }

        return JsonResponse(response, status=200)
    except Exception as error:
        if isinstance(error, AppError) or isinstance(error, AppValidatorError):
            return JsonResponse({'message': error.message}, status=error.statusCode)
        return JsonResponse({'message': 'Internal server error'}, status=500)