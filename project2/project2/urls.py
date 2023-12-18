from django.contrib import admin
from django.urls import path
from django.views import View
from main.views import MyView, LogoutView  

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', MyView.as_view(), name='home'),
    path('logout/', LogoutView.as_view(), name='logout'), 
]
