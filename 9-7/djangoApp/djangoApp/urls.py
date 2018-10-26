from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import LoginView
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('login/', views.login_view, name='login'),
    path('create_user/', views.create_user, name='create_user'),
    path('create_user_view/', views.create_user_view),
    path('logout/', views.logout_view),
    path('accounts/login/', LoginView.as_view(template_name='login_view.html')),
]
