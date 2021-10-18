from django.urls import path
from .views import view_products, delete, add, edit_name

urlpatterns = [
    path('', view_products, name='news'),
    path('add/', add, name="add"),
    path('<str:name>/delete/', delete, name='delete'),
    path('<str:name>/edit/', edit_name, name='edit'),

]
# path(podstrona, funkcja(z_widoku), nazwa_endpointu)
#podstronę definiujemy w urlpatterns w głównej apce. Tutaj tylko podstrony podstrony.

