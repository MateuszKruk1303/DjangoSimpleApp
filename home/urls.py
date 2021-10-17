from django.urls import path
from .views import index

urlpatterns = [
    path('', index, name='index'),
]
# path(podstrona, funkcja(z_widoku), nazwa_endpointu)