from django.db.models import query
from rest_framework.serializers import Serializer
from Animal.models import Animal
from .serializers import AnimalSerializer
from rest_framework.viewsets import ModelViewSet

class AnimalViewSet(ModelViewSet):
    # queryset = Animal.objects.all()
    serializer_class = AnimalSerializer

    def get_queryset(self):
        nome_popular = self.request.query_params.get('nome_popular', None)
        raca = self.request.query_params.get('raca', None)
        origem = self.request.query_params.get('origem', None)
        nome_cientifico = self.request.query_params.get('cientifico', None)
        queryset = Animal.objects.all()
        presente = False

        if nome_popular:
            presente = nome_popular.lower() in "gatos" 
        
        if presente:
            queryset = Animal.objects.filter(nome_popular__iexact=nome_popular)
        
            if raca:
                queryset.filter(raca__iexact=raca)

            if origem:
                queryset.filter(origem__iexact=origem)
            
            if nome_cientifico:
                queryset.filter(nome_cientifico__iexact=nome_cientifico)

        return queryset
    