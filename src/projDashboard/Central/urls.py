from django.urls import path
from .views import DashboardView, void_view

urlpatterns = [
    # Redirecionamento
    path('', void_view, name='Void'),
    # Pág. Principal
    path('dashboard/', DashboardView.as_view(), name='Dashboard'),
]