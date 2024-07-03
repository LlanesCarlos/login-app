from django.http import HttpResponseRedirect
from django.utils.deprecation import MiddlewareMixin


class AuthMiddleware(MiddlewareMixin):
    def process_response(self, request, response):
        if not request.user.is_authenticated and request.path != '/accounts/login/' and request.path != '/accounts/signup/':
            return HttpResponseRedirect('/accounts/login/')
        return response