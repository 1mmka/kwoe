from django.views.generic import View
from django.http import HttpResponse
import requests
from django.conf import settings

class MyView(View):
    def get(self,request,*args,**kwargs):
        token_url = "http://127.0.0.1:8000/token/"
        
        data = {
            'username' : 'admin',
            'password' : 'admin',
        }
        
        token_response = requests.post(token_url,data=data)
        if token_response.status_code == 200:
            access_token = token_response.json()['access']
            refresh_token = token_response.json()['refresh']
            
            response = HttpResponse('Токены успешно были созданы!')
            
            response.set_cookie('access',access_token,
                max_age=settings.AUTH_COOKIE_ACCESS_MAX_AGE,
                path=settings.AUTH_COOKIE_PATH,
                secure=settings.AUTH_COOKIE_SECURE,
                httponly=settings.AUTH_COOKIE_HTTP_ONLY,
                samesite=settings.AUTH_COOKIE_SAMESITE)
            
            response.set_cookie('refresh',refresh_token,
                max_age=settings.AUTH_COOKIE_REFRESH_MAX_AGE,
                path=settings.AUTH_COOKIE_PATH,
                secure=settings.AUTH_COOKIE_SECURE,
                httponly=settings.AUTH_COOKIE_HTTP_ONLY,
                samesite=settings.AUTH_COOKIE_SAMESITE)
            
            return response
        else:
            return HttpResponse('Возникла проблема!')