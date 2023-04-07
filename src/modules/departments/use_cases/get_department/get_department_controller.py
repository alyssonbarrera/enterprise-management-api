from django.http import JsonResponse
from src.shared.errors.AppError import AppError
from src.modules.departments.use_cases.get_department.make_get_department_use_case import make_get_department_use_case

def get_department_controller(request, id):
    try:
        use_case = make_get_department_use_case()
        department = use_case.execute(id)

        response = {
            'department': department.to_dict(),
        }

        return JsonResponse(response, status=200)
    
    except Exception as error:
        if isinstance(error, AppError):
            return JsonResponse({'message': error.message}, status=error.statusCode)
        else:
            return JsonResponse({'message': 'Internal server error'}, status=500)