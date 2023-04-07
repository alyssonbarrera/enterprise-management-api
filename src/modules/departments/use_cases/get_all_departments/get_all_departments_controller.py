from django.http import JsonResponse
from src.modules.departments.use_cases.get_all_departments.make_get_all_departments_use_case import make_get_all_departments_use_case

def get_all_departments_controller(request):
    page = request.GET.get('page', 1)

    try:
        use_case = make_get_all_departments_use_case()
        departments = use_case.execute(page)

        response = {
            'departments': departments,
        }

        return JsonResponse(response, status=200)
    except:
        return JsonResponse({'message': 'Internal server error'}, status=500)