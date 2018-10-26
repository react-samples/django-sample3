from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('session_count/', views.session_count),
    path('session_flush/', views.session_flush),
]
