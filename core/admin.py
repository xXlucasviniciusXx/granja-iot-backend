from django.contrib import admin
from .models import Granja, Galpao, Sensor, Leitura, Atuador, RegraAutomacao

@admin.register(Granja)
class GranjaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'localizacao', 'responsavel')


@admin.register(Galpao)
class GalpaoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'granja', 'capacidade_aves')


@admin.register(Sensor)
class SensorAdmin(admin.ModelAdmin):
    list_display = ('nome', 'tipo', 'galpao', 'unidade')


@admin.register(Leitura)
class LeituraAdmin(admin.ModelAdmin):
    list_display = ('sensor', 'valor', 'data_hora')
    list_filter = ('sensor', 'data_hora')


@admin.register(Atuador)
class AtuadorAdmin(admin.ModelAdmin):
    list_display = ('nome', 'tipo', 'galpao', 'estado')


@admin.register(RegraAutomacao)
class RegraAutomacaoAdmin(admin.ModelAdmin):
    list_display = ('galpao', 'sensor', 'atuador', 'condicao', 'valor_referencia', 'ativo')

