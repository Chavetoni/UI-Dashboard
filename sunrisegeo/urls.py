
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path

app_name = 'client_portal'

urlpatterns = [
     # Authentication URLs using Django's built-in views
    path('login/', auth_views.LoginView.as_view(template_name='portal/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    # --- ADD THIS LINE for the root path ---
    path('', views.index, name='index'), # Maps the empty path to the index view

    # Your other custom views
    path('dashboard/', views.dashboard, name='dashboard'), # Path for the dashboard view
    path('projects/<int:project_id>/', views.project_detail, name='project_detail'), # Path for project detail
]
    

