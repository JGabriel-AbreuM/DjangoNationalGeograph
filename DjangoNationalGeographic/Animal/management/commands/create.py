from django.core.management.base import BaseCommand
from Animal.models import Animal
from Protecao.models import Protecao
from random import randrange

class Command(BaseCommand):
    help = 'OOOOO Jacaré'
  
    def handle(self, *args, **kwargs):
        tipos = Protecao.objects.all()
        for i in range(3):
            raca = input("Raca: ")
            origem = input("Origem: ")
            nome = input("Nome: ")
            nome_cientifico = input("Nome Científico: ")
            num = 0

            for p in tipos:
                print(f"[{num}] - {p}")
                num += 1

            protecao = int(input("Proteção: "))
            Animal.objects.create(
                raca=raca, 
                origem=origem,
                nome_popular=nome,
                nome_cientifico=nome_cientifico,
                protecao=tipos[protecao]
            )
            print()

        print('Animais cadastrados com sucesso')
