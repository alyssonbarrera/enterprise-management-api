from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from .make_get_all_employees_use_case import make_get_all_employees_use_case

@require_http_methods(['GET'])
def get_all_employees_controller(request):
    page = request.GET.get('page', 1) or 1

    use_case = make_get_all_employees_use_case()

    employees = use_case.execute(page)

    response = {
        'employees': employees,
    }
    
    return JsonResponse(response, status=200)
