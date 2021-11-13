from django.test import TestCase
from .models import Animal, Raca, Origem, NomePopular, NomeCientifico
from Protecao.models import Protecao

class AnimalTestCase(TestCase):
    def setUp(self):
        self.protecao=Protecao.objects.create(
            tipo="Penas"
        )

        self.raca = Raca.objects.create(
            raca = "v"   
        )

        self.origem = Origem.objects.create(
            origem = "Afeganistão"
        )

        self.nome_popular = NomePopular.objects.create(
            nome_popular = "g"
        )

        self.nome_cientifico = NomeCientifico.objects.create(
            nome_cientifico = "yy"
        )
        
        self.animal = Animal.objects.create(
            raca=self.raca,
            origem=self.origem,
            nome_popular=self.nome_popular,
            nome_cientifico=self.nome_cientifico,
            protecao=self.protecao,
        )                                      

    def test_animal_contido(self):
       self.assertIn(self.animal, Animal.objects.all())

    def test_protecao_contido(self):
        item = Protecao.objects.create(
            tipo="z"
        )

        self.assertIn(item, Protecao.objects.all())

    def test_animal_filter(self):
        raca_nova = Raca.objects.create(
            raca = "x"
        ) 

        item = Animal.objects.create(
            raca=raca_nova,
            origem=self.origem,
            nome_popular=self.nome_popular,
            nome_cientifico=self.nome_cientifico,
            protecao=self.protecao, 
        )             

        self.assertNotIn(item, Animal.objects.filter(raca=self.raca))
        self.assertIn(self.animal, Animal.objects.filter(raca=self.raca))
