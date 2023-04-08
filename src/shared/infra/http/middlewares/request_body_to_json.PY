import json
from django.http import HttpResponse

class RequestBodyToJson:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.method in ['POST', 'PUT', 'PATCH'] and 'application/json' in request.content_type:
            try:
                request.json = json.loads(request.body.decode('utf-8'))
            except ValueError:
                return HttpResponse({'message': 'Invalid format'}, status=400)

        response = self.get_response(request)

        return response
