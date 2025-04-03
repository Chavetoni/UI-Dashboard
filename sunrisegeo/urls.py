from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # Include client_portal URLs
    path('', include('client_portal.urls')),
]