from rest_framework import routers
from django.urls import path, include
from .views import (
    GranjaViewSet, GalpaoViewSet, SensorViewSet,
    LeituraViewSet, AtuadorViewSet, RegraAutomacaoViewSet
)

router = routers.DefaultRouter()
router.register(r'granjas', GranjaViewSet)
router.register(r'galpoes', GalpaoViewSet)
router.register(r'sensores', SensorViewSet)
router.register(r'leituras', LeituraViewSet)
router.register(r'atuadores', AtuadorViewSet)
router.register(r'regras', RegraAutomacaoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
