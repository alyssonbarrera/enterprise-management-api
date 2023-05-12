from django.http import JsonResponse
from src.utils.uuid_validator import uuid_validator
from django.views.decorators.http import require_http_methods
from .make_fetch_project_metrics_use_case import make_fetch_project_metrics_use_case

@require_http_methods(['GET'])
def fetch_project_metrics_controller(request, id):
    if not id:
        return JsonResponse({'message': 'Id is required'}, status=400)
    
    id = uuid_validator(id)['id']
    
    use_case = make_fetch_project_metrics_use_case()

    project_metrics = use_case.execute(id)

    response = {
        'metrics': project_metrics
    }

    return JsonResponse(response, status=200)
