
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated

from mundial_api.serializers import EquipoSerializer, JugadorSerializer
from mundial_api.models import Jugador, Equipo

def listarEquipos(request):
    datos = {
        "Equipos": [
            {"nombre": "real madrid", "año_creacion": "1902", "Campeon": True, "imagen": "img/CopaDeEuropa.png"},
            {"nombre": "barcelona", "año_creacion":"1899", "Campeon": False, "imagen": "img/false.png"},
            {"nombre": "la roja", "año_creacion": "1895", "Campeon": True, "imagen": "img/check.png"}
        ]
    }
    return render(request, 'Equipos_app/listar_equipo.html', datos)


@csrf_exempt
@permission_classes((AllowAny,))
def verEquipos(request):
    try:
        equipo= Equipos.objects.filter(id=id).first
        data={'equipo': equipo}
        return render(request, 'Equipos_app/Ver_equipo.html' , data)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
