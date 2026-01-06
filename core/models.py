from django.db import models

from django.db import models


class Granja(models.Model):
    nome = models.CharField(max_length=100)
    localizacao = models.CharField(max_length=150, blank=True, null=True)
    responsavel = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.nome


class Galpao(models.Model):
    nome = models.CharField(max_length=100)
    granja = models.ForeignKey(Granja, on_delete=models.CASCADE, related_name='galpoes')
    capacidade_aves = models.IntegerField(default=0)
    descricao = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.nome} ({self.granja.nome})"


class Sensor(models.Model):
    TIPO_CHOICES = [
        ('temperatura', 'Temperatura'),
        ('umidade', 'Umidade'),
        ('gases', 'Gases'),
        ('luminosidade', 'Luminosidade'),
        ('outro', 'Outro'),
    ]
    nome = models.CharField(max_length=100)
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES)
    galpao = models.ForeignKey(Galpao, on_delete=models.CASCADE, related_name='sensores')
    unidade = models.CharField(max_length=10, default='')

    def __str__(self):
        return f"{self.nome} - {self.tipo}"


class Leitura(models.Model):
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='leituras')
    valor = models.FloatField()
    data_hora = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.sensor.nome} = {self.valor}{self.sensor.unidade} ({self.data_hora.strftime('%d/%m %H:%M')})"


class Atuador(models.Model):
    TIPO_CHOICES = [
        ('ventilador', 'Ventilador'),
        ('luz', 'Luz'),
        ('bomba_agua', 'Bomba de Água'),
        ('aquecedor', 'Aquecedor'),
    ]
    nome = models.CharField(max_length=100)
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES)
    galpao = models.ForeignKey(Galpao, on_delete=models.CASCADE, related_name='atuadores')
    estado = models.BooleanField(default=False)  # True = ligado

    def __str__(self):
        return f"{self.nome} - {'Ligado' if self.estado else 'Desligado'}"


class RegraAutomacao(models.Model):
    galpao = models.ForeignKey(Galpao, on_delete=models.CASCADE, related_name='regras')
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='regras')
    atuador = models.ForeignKey(Atuador, on_delete=models.CASCADE, related_name='regras')
    condicao = models.CharField(max_length=10, choices=[('>', 'Maior que'), ('<', 'Menor que')])
    valor_referencia = models.FloatField()
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return f"Se {self.sensor.nome} {self.condicao} {self.valor_referencia}, acionar {self.atuador.nome}"