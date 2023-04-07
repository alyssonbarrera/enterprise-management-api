from django.http import JsonResponse
from src.shared.errors.AppError import AppError
from src.modules.departments.use_cases.create_department.make_create_department_use_case import make_create_department_use_case

def create_department_controller(request):
    try:
        data = request.json
        use_case = make_create_department_use_case()

        department = use_case.execute(data)

        response = {
            'department': department,
        }

        return JsonResponse(response, status=201)
    except Exception as error:
        if isinstance(error, AppError):
            return JsonResponse({'message': error.message}, status=error.statusCode)
        else:
            return JsonResponse({'message': 'Internal server error'}, status=500)