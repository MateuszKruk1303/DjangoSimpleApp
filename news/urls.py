from django.urls import path
from .views import view_news

urlpatterns = [
    path('', view_news, name='news'),
]
# path(podstrona, funkcja(z_widoku), nazwa_endpointu)
#podstronę definiujemy w urlpatterns w głównej apce. Tutaj tylko podstrony podstrony.