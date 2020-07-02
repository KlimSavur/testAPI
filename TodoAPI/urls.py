from django.contrib import admin
from django.urls import path
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', views.api_view.as_view(), name = 'api'),
    path('api<pk>/', views.api_detail.as_view(), name = 'api_detail'),
    ]

