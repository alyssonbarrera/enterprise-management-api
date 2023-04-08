from django.http import JsonResponse
from src.shared.errors.AppError import AppError
from django.views.decorators.http import require_http_methods
from .make_get_employee_use_case import make_get_employee_use_case

@require_http_methods(['GET'])
def get_employee_controller(request, id):
    try:
        use_case = make_get_employee_use_case()
        employee = use_case.execute(id)

        response = {
            'employee': employee
        }

        return JsonResponse(response, status=200)
    except Exception as error:
        if isinstance(error, AppError):
            return JsonResponse({'message': error.message}, status=error.statusCode)
        else:
            print('CAIU AQUI', error)
            return JsonResponse({'message': 'Internal server error'}, status=500)
    