from django.db import models
from django.db.models.base import Model
from Protecao.models import Protecao

class Animal(models.Model):
    raca = models.CharField(max_length=255, null=False, blank=False)
    origem = models.CharField(max_length=255, null=False, blank=False)
    nome_popular = models.CharField(max_length=255, null=False, blank=False)
    nome_cientifico = models.CharField(max_length=255, null=False, blank=False)
    protecao = models.ForeignKey(Protecao, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nome_popular} - {self.raca}"
