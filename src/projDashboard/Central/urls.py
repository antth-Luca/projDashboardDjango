from django.urls import path
from .views import PagPrincipal

urlpatterns = [
    path('', PagPrincipal.as_view(), name='PagPrincipal'),
]