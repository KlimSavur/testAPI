from django.contrib import admin
from django.urls import path
from api import views
from rest_framework_jwt.views import obtain_jwt_token
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-token-auth/', obtain_jwt_token, name='create-token'),
    path('api/', views.api_view.as_view(), name = 'api'),
    path('api<pk>/', views.api_detail.as_view(), name = 'api_detail'),
    path('auth/login/', views.login_view.as_view(), name = 'auth-login'),
    path('auth/register/', views.register_view.as_view(), name= 'auth-register'),
    ]

