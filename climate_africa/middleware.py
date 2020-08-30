from django.shortcuts import redirect
from django.conf import settings

def requires_authentication(request):
    return not request.path_info in [settings.LOGIN_URL] + getattr(settings, 'OPEN_URLS', [])

class RequireLoginMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if False:#not request.user.is_authenticated and requires_authentication(request):
            return redirect(f'/login/?next={request.path}')
        else:
            return self.get_response(request)
