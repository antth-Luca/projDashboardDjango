from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # Admin
    path('admin-dashboard/', admin.site.urls),
    # Módulos
    path('', include('Central.urls')),
    path('', include('Contas.urls')),
]
