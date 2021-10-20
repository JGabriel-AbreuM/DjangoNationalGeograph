from django.db import models

class Protecao(models.Model):
    tipo = models.CharField(max_length=255, null=False, blank=False)

    def __str__(self):
        return self.tipo