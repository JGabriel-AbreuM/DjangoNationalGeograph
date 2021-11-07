from django.db import models
from django.db.models.base import Model
from Protecao.models import Protecao

class Raca(models.Model):
    raca = models.CharField(max_length=255, null=False, blank=False)
    
    def __str__(self) -> str:
        return self.raca

class Origem(models.Model):
    origem = models.CharField(max_length=255, null=False, blank=False)
    
    def __str__(self) -> str:
        return self.origem

class NomePopular(models.Model):
    nome_popular = models.CharField(max_length=255, null=False, blank=False)

    def __str__(self) -> str:
        return self.nome_popular

class NomeCientifico(models.Model):
    nome_cientifico = models.CharField(max_length=255, null=False, blank=False)

    def __str__(self) -> str:
        return self.nome_cientifico
    
class Animal(models.Model):
    raca = models.ForeignKey(Raca, on_delete=models.CASCADE)
    origem = models.ForeignKey(Origem, on_delete=models.CASCADE)
    nome_popular = models.ForeignKey(NomePopular, on_delete=models.CASCADE)
    nome_cientifico = models.ForeignKey(NomeCientifico, on_delete=models.CASCADE)
    foto = models.ImageField(upload_to="imagens/")
    protecao = models.ForeignKey(Protecao, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nome_popular} - {self.raca}"
