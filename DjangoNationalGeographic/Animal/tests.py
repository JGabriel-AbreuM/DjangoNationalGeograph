from django.test import TestCase
from .models import Animal
from Protecao.models import Protecao

class AnimalTestCase(TestCase):
    def setUp(self):
        self.protecao=Protecao.objects.create(
            tipo="Penas"
        )
        self.animal = Animal.objects.create(
            raca="x",
            origem="y",
            nome_popular="z",
            nome_cientifico="a",
            protecao=self.protecao,
        )                                      

    def test_animal_contido(self):
        item = Animal.objects.create(
            raca="x",
            origem="y",
            nome_popular="z",
            nome_cientifico="a",
            protecao=self.protecao,
        )                

        self.assertIn(item, Animal.objects.all())

    def test_protecao_contido(self):
        item = Protecao.objects.create(
            tipo="z"
        )

        self.assertIn(item, Protecao.objects.all())