'''Tarefa: Escreva um programa que simule sua jornada heróica pela masmorra.
 O programa deve percorrer cada sala e verificar se há tesouros ou monstros.
 Se você encontrar um tesouro, colecionará a recompensa. Se encontrar um monstro, terá que derrotá-lo para continuar.

Atenção
Em nossa resolução utilizamos a função.includes() do JavaScript para verificar se
um número (representando a sala atual) está presente nos arrays salasComTesouro e salasComMonstro.

Entrada
O número total de salas no dungeon (um número inteiro).

Saída
Sempre que encontrar um tesouro, imprima " Tesouro na sala X!".

Sempre que encontrar um monstro, imprima "Monstro na sala X!".'''

from random import randint
from time import sleep

class Masmorra:
    def __init__(self, salas, tesouro, monstro):
        self.salas = salas
        self.monstro = monstro
        self.tesouro = tesouro

    def sala_vazia(self):
        return self.salas >= self.monstro and self.salas >= self.tesouro

    def sala_monstro(self):
        return self.salas < self.monstro

    def sala_tesouro(self):
        return self.salas < self.tesouro

    def proxima_sala(self, n):
        return n + 1

def tesouro_monstro_sala():
    salas = 10
    sala_atual = 1
    print('- -' * 20)
    print(f'Essa masmorra tem {salas} salas para serem passadas.')
    print('- -' * 20)
    sleep(2)

    while sala_atual <= salas:
        tesouro = randint(1, 15)
        monstro = randint(1, 20)
        masmorra = Masmorra(salas, tesouro, monstro)
        print('__' * 20)
        print(f'\nEntrando na {sala_atual} sala...')
        sleep(2)

        if masmorra.sala_monstro():
            print(' ' * 20)
            print(f'\nVocê encontrou um monstro!!! Hora de lutar!!!')

            sleep(2)
            if monstro > 18 :
                print('Esse monstro é muito mais forte do que você!')
                sleep(2)
                lutar = int(input('Você deseja continuar a luta ou correr? \n[1] - lutar \n[2] - correr\n'))
                sleep(2)
                if lutar == 1 and tesouro > 7:
                    print('Infelizmente você sucumbiu ao poder do monstro.')
                    sleep(2)
                    break
                elif lutar == 1 and tesouro < 7:
                    print('Com sua determinação, você conseguiu derrotar o monstro')
                    sleep(2)
                    print('Coletando itens dropados...')
                    sleep(2)
                elif lutar == 2 and tesouro > 3:
                    print('Você correu do monstro...')
                    sleep(2)
                else:
                    sleep(2)
                    print('O monstro te alcançou\n'
                          'Você morreu!!!!')

        elif masmorra.sala_tesouro():
            print(' ' * 20)
            sleep(2)
            print(f'Você encontrou um tesouro! Hora de ficar rico!!')
            sleep(2)
            print('Tentando abrir o baú...')
            sleep(2)
            if tesouro > 10:
                print('Baú aberto com sucesso')
                sleep(2)
            else:
                print('O tesouro era uma armadilha')
                sleep(2)

        elif masmorra.sala_vazia():
            print(' ' * 20)
            print(f'Essa sala está limpa, nada para encontrar.')
            sleep(2)
            print('Passando pela sala...')
            sleep(2)
            if tesouro == monstro:
                print('Havia um monstro escondido.')
                sleep(1)
                lutar = int(input('Lutar ou correr?\n[1] - lutar\n[2] - correr\n: '))
                sleep(2)
                if lutar == 1 and monstro > 15:
                    print('\nVocê morreu!!')
                    break
                elif lutar == 1 and monstro <= 15:
                    print('\nVocê derrotou o monstro!!')
                    sleep(1)
                    print('\nColetando itens dropados...')
                    sleep(2)
                elif lutar == 2 and monstro > 18:
                    sleep(1)
                    print('O monstro era rápido demais, você morreu!!')
                    break
                elif lutar == 2 and monstro <= 18:
                    sleep(1)
                    print('Você conseguiu fugir e está indo para a próxima sala...')
                    sleep(2)
                else:
                    continue
        else:
            continue

        sala_atual = masmorra.proxima_sala(sala_atual)

def main():
    tesouro_monstro_sala()

main()

