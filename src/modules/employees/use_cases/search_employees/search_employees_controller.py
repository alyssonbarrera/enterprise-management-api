from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from src.modules.employees.use_cases.search_employees.make_search_employees_use_case import make_search_employees_use_case

@require_http_methods(['GET'])
def search_employees_controller(request):
    try:
        query = request.GET.get('query')
        page = request.GET.get('page', 1) or 1

        use_case = make_search_employees_use_case()
        employees = use_case.execute(query, page)

        response = {
            'employees': employees
        }

        return JsonResponse(response, status=200)
    except:
        return JsonResponse({'message': 'Internal server error'}, status=500)