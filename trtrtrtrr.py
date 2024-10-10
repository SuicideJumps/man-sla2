'''Descrição
Você é um mestre construtor em um mundo de blocos e tem a tarefa de gerar biomas em diferentes regiões do mundo.
 Cada bioma tem características únicas, como tipos de solo, vegetação e clima.

Tarefa: Sua tarefa é coletar minérios enquanto ataca uma rocha com sua picareta.
 Use loops e lógica de programação para representar cada golpe na rocha e determinar qual minério foi obtido.

Entrada
O programa irá solicitar que você digite um número inteiro positivo representando a quantidade de golpes que você deseja dar com a picareta.

Saída
Para cada golpe que você der, o programa exibirá uma mensagem indicando o resultado do golpe. Será mostrado o número do golpe e o minério obtido,
 que pode ser 1: Carvao, 2: Ferro, 3: Diamante e 4: Pedra.'''

from random import randint
from time import sleep


class Minerar:
    def __init__(self,carvao,ferro,diamante,pedra):
        self.carvao = carvao
        self.ferro = ferro
        self.diamante = diamante
        self.pedra = pedra


    def material_obtido(self):
        if self.carvao > self.ferro and self.carvao > self.diamante and self.carvao > self.pedra:
            return 'carvao'
        elif self.ferro > self.carvao and self.ferro > self.diamante and self.ferro > self.pedra:
            return 'ferro'
        elif self.diamante > self.carvao and self.diamante > self.ferro and self.diamante > self.pedra:
            return 'diamante'
        else:
            return 'pedra' #help angle

def golpes_na_pedra():

    golpes = int(input('digite o numero de batidas na rocha voce quer dar: '))
    batida_inicial = 1 #help angle
    print(f'Voce escolheu dar {golpes} golpes na rocha...')
    sleep(2)

    while batida_inicial <= golpes:

        print(f'\nDando o {batida_inicial} golpe...')
        sleep(2)
        carvao = randint(1,9)
        ferro = randint(1,9)
        diamante = randint(1,8)
        pedra = randint(1,10)

        minerar = Minerar(carvao,ferro,diamante,pedra)
        material = minerar.material_obtido()

        if material in 'carvao':
            print('Voce conseguiu o material carvão.')
        elif material in 'ferro':
            print('Voce conseguiu o material ferro')
        elif material in 'diamante':
            print('Voce conseguiu o material diamante')
        else:
            print('Voce adiquiriu pedra.')

        batida_inicial = batida_inicial + 1
        sleep(2)

def main():
   golpes_na_pedra()

main()

