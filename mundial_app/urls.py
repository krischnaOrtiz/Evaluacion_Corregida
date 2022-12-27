from django.urls import path

from mundial_app import views


urlpatterns = [
    path('equipo/listaEquipos/', views.listarEquipos),
    path('equipo/listaEquipos/<int:id>', views.verEquipos),
    path('equipo/', views.verEquipos),
    path('equipo/<int:id>', views.verEquipos)
]