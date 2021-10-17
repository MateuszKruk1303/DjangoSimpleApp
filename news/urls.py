from django.urls import path
from .views import view_news, add, get, delete, edit_title

urlpatterns = [
    path('', view_news, name='news'),
    path('add/', add, name="add"),
    path('<int:id>/', get, name='get'),
    path('<str:topic>/delete/', delete, name='delete'),
    path('<str:topic>/edit/', edit_title, name='edit'),

]
# path(podstrona, funkcja(z_widoku), nazwa_endpointu)
#podstronę definiujemy w urlpatterns w głównej apce. Tutaj tylko podstrony podstrony.

