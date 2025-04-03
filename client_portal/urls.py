from django.urls import path 
from django.contrib.auth import views as auth_views
from . import views

app_name = 'client_portal'

urlpatterns = [
    path('', views.index, name='index'), 
    path('login', auth_views.LoginView.as_view(template_name='client_portal/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'), 
    path('dashboard', views.dashboard, name='dashboard'),
    path('projects/<int:project_id>/', views.project_detail, name='project_detail'),  
]