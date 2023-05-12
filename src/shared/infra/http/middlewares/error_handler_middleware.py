# myapp/middleware/error_middleware.py

from django.http import JsonResponse
from src.shared.errors.AppError import AppError
from src.shared.errors.AppValidatorError import AppValidatorError

class ErrorHandlerMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_exception(self, request, exception):
        if isinstance(exception, AppError):
            return JsonResponse({'message': exception.message}, status=exception.status_code)
        elif isinstance(exception, AppValidatorError):
            return JsonResponse({'message': exception.message}, status=exception.status_code)
        else:
            return JsonResponse({'message': 'Internal server error'}, status=500)

