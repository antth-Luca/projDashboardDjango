from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # Módulos
    path('', include('Central.urls')),
    path('', include('Contas.urls')),
]
