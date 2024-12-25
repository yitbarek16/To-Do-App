# middleware.py

from django.shortcuts import redirect
from django.urls import reverse

class RedirectToSignupMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if not request.user.is_authenticated and request.path not in [reverse('signup'), reverse('login')]:
            return redirect('signup')
        response = self.get_response(request)
        return response 
