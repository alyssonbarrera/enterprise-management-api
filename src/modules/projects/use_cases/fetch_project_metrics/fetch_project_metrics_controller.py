from django.http import JsonResponse
from src.shared.errors.AppError import AppError
from django.views.decorators.http import require_http_methods
from .make_fetch_project_metrics_use_case import make_fetch_project_metrics_use_case

@require_http_methods(['GET'])
def fetch_project_metrics_controller(request, id):
    try:
        if not id:
            return JsonResponse({'message': 'Id is required'}, status=400)
        
        use_case = make_fetch_project_metrics_use_case()
        project_metrics = use_case.execute(id)

        return JsonResponse(project_metrics, status=200)
    except Exception as error:
        if isinstance(error, AppError):
            return JsonResponse({'message': error.message}, status=error.statusCode)
        return JsonResponse({'message': 'Internal server error'}, status=500)
