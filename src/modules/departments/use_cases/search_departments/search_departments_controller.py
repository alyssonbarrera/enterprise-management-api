from django.http import JsonResponse
from src.modules.departments.use_cases.search_departments.make_search_departments_use_case import make_search_departments_use_case

def search_departments_controller(request):
    try:
        query = request.GET.get('query')
        use_case = make_search_departments_use_case()
        departments = use_case.execute(query)

        response = {
            'departments': departments
        }

        return JsonResponse(response, safe=False)
    except:
        return JsonResponse({'message': 'Internal server error'}, status=500)