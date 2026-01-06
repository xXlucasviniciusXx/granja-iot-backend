from rest_framework import serializers
from .models import Granja, Galpao, Sensor, Leitura, Atuador, RegraAutomacao


class GranjaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Granja
        fields = '__all__'


class GalpaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Galpao
        fields = '__all__'


class SensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = '__all__'


class LeituraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Leitura
        fields = '__all__'


class AtuadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Atuador
        fields = '__all__'


class RegraAutomacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegraAutomacao
        fields = '__all__'
