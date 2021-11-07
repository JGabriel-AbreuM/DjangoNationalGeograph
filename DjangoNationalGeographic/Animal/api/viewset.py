from django.db.models import query
from rest_framework.serializers import Serializer
from Animal.models import Animal
from .serializers import AnimalSerializer
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend

class AnimalViewSet(ModelViewSet):
    queryset = Animal.objects.all()
    serializer_class = AnimalSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['nome_popular', 'raca', 'origem', 'nome_cientifico']

    
