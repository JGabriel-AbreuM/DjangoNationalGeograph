from django.core.management.base import BaseCommand
from Animal.models import Animal, Raca, Origem, NomePopular, NomeCientifico
from Protecao.models import Protecao

class Command(BaseCommand):
  
    def handle(self, *args, **kwargs):
        tipos_protecao = Protecao.objects.all()
        tipos_raca = Raca.objects.all()
        tipos_origem = Origem.objects.all()
        tipos_nome_popular = NomePopular.objects.all()
        tipos_nome_cientifico = NomeCientifico.objects.all()

        for i in range(3):
            num = 0
            for p in tipos_raca:
                print(f"[{num}] - {p}")
                num += 1

            raca = int(input("Raça: "))

            num = 0
            for p in tipos_origem:
                print(f"[{num}] - {p}")
                num += 1

            origem = int(input("Origem: "))

            num = 0
            for p in tipos_nome_popular:
                print(f"[{num}] - {p}")
                num += 1

            nome_popular = int(input("Nome Popular: "))
            
            num = 0
            for p in tipos_nome_cientifico:
                print(f"[{num}] - {p}")
                num += 1

            nome_cientifico = int(input("Nome Cientifico: "))
            num = 0

            for p in tipos_protecao:
                print(f"[{num}] - {p}")
                num += 1

            protecao = int(input("Proteção: "))
            Animal.objects.create(
                raca=tipos_raca[raca], 
                origem=tipos_origem[origem],
                nome_popular=tipos_nome_popular[nome_popular],
                nome_cientifico=tipos_nome_cientifico[nome_cientifico],
                protecao=tipos_protecao[protecao]
            )
            print()

        print('Animais cadastrados com sucesso')
