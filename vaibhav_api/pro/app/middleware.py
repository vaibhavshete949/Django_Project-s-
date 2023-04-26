from django.http import JsonResponse
from threading import Lock

class RequestCounterMiddleware:
    
    def __init__(self, get_response):
        self.get_response = get_response
        self.counter = 0
        self.counter_lock = Lock()

    def __call__(self, request):
        # Increment the counter for each request
        with self.counter_lock:
            self.counter += 1
        response = self.get_response(request)
        return response

    def process_view(self, request, view_func, view_args, view_kwargs):
        # Check if the request is for the request count endpoint
        if request.path == '/count/':
            # Return the current request count
            with self.counter_lock:
                response_data = {"requests": self.counter}
                return JsonResponse(response_data)

    def process_request(self, request):
        # Check if the request is for resetting the request count
        if request.path == '/count/reset/' and request.method == 'POST':
            # Reset the request count
            with self.counter_lock:
                self.counter = 0
                response_data = {"message": "request count reset successfully"}
                return JsonResponse(response_data)
        return None
