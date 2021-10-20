from django.db import models
from rest_framework.serializers import ModelSerializer
from Animal.models import Animal

class AnimalSerializer(ModelSerializer):
    class Meta:
        model = Animal
        fields = [
            "id", 
            "raca",
            "origem",
            "nome_popular",
            "nome_cientifico",
            "protecao"
        ]