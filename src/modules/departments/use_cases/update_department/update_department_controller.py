from src.shared.errors.AppError import AppError
from django.http import JsonResponse
from src.modules.departments.use_cases.update_department.make_update_department_use_case import make_update_department_use_case

def update_department_controller(request, id):
    try:
        data = request.json

        use_case = make_update_department_use_case()

        department = use_case.execute(id, data)

        response = {
            'department': department
        }

        return JsonResponse(response, status=200)
    except Exception as error:
        if isinstance(error, AppError):
            return JsonResponse({'message': error.message}, status=error.statusCode)
        return JsonResponse({'message': 'Internal server error'}, status=500)