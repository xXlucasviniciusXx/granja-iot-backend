from django.shortcuts import render

from rest_framework import viewsets
from .models import Granja, Galpao, Sensor, Leitura, Atuador, RegraAutomacao
from .serializers import (
    GranjaSerializer, GalpaoSerializer, SensorSerializer,
    LeituraSerializer, AtuadorSerializer, RegraAutomacaoSerializer
)


class GranjaViewSet(viewsets.ModelViewSet):
    queryset = Granja.objects.all()
    serializer_class = GranjaSerializer


class GalpaoViewSet(viewsets.ModelViewSet):
    queryset = Galpao.objects.all()
    serializer_class = GalpaoSerializer


class SensorViewSet(viewsets.ModelViewSet):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


class LeituraViewSet(viewsets.ModelViewSet):
    queryset = Leitura.objects.all().order_by('-data_hora')
    serializer_class = LeituraSerializer


class AtuadorViewSet(viewsets.ModelViewSet):
    queryset = Atuador.objects.all()
    serializer_class = AtuadorSerializer


class RegraAutomacaoViewSet(viewsets.ModelViewSet):
    queryset = RegraAutomacao.objects.all()
    serializer_class = RegraAutomacaoSerializer
