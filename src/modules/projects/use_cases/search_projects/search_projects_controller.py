from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from .make_search_projects_use_case import make_search_projects_use_case

@require_http_methods(['GET'])
def search_projects_controller(request):
    query = request.GET.get('query')

    page = request.GET.get('page', 1) or 1

    use_case = make_search_projects_use_case()

    projects = use_case.execute(query, page)

    response = {
        'projects': projects
    }
    
    return JsonResponse(response, status=200)
