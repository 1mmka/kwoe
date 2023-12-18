from django.contrib import admin
from django.urls import path,include
from rest_framework.routers import SimpleRouter
from app.views import UsersViewSet

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

router = SimpleRouter()
router.register('site',UsersViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    
    # SIMPLE-JWT TOKENS
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    # DJORES USER
    path('auth/', include('djoser.urls')), # для работы с пользователями   
    
    
] + router.urls