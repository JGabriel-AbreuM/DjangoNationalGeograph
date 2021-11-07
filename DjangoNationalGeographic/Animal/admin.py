from django.contrib import admin
from .models import Animal, Raca, NomeCientifico, Origem, NomePopular

admin.site.register(Animal)
admin.site.register(Raca)
admin.site.register(Origem)
admin.site.register(NomeCientifico)
admin.site.register(NomePopular)
