'''Descrição
Imagine um universo onde você é um Mestre Pokémon com o poder de criar novas criaturas através da combinação de nomes
 Seu algoritmo é a chave para dar vida a esses seres incríveis. Você receberá uma primeira parte do nome de um Pokémon
  e sua tarefa é completá-la com o sufixo mágico adequado, revelando o nome completo do Pokémon.

Tarefa: Sua missão é criar uma função extraordinária chamada combinarNomePokemon.
 Essa função possui um toque mágico que transforma uma entrada simples em algo verdadeiramente especial.

Entrada
A entrada consistirá em uma única string representando a primeira parte do nome de um Pokémon.

Saída
A função deve retornar uma nova string que é a combinação da parte inicial(Préfixo) do nome do Pokémon com o sufixo
 final do nome, formando um nome de Pokémon completo.
from time import sleep


def combinar_nome_pokemon():
    nome_pokemon = str(input('Digite o nome do pokemon: ')).strip()
    sleep(2)
    print('Evoluindo o pokemon...')
    print(f'{nome_pokemon} evoluiu para {nome_pokemon}sauro')

def main():
    combinar_nome_pokemon()
main()'''

def combinarNomePokemon(prefixo):
    if prefixo == 'Pika':
        return 'Pikachu'
    elif prefixo == 'Bulba':
        return 'Bulbasaur'
    elif prefixo == 'Char':
        return 'Charmander'
    elif prefixo == 'Squir':
        return 'Squirtle'
    elif prefixo == 'Eevee':
        return 'Eeveeon'
    elif prefixo == 'Mag':
        return 'Magmar'
    elif prefixo == 'Mew':
        return 'Mewtwo'
    else:
        return "Prefixo não encontrado!"

# Testando a função
print(combinarNomePokemon('Pika'))
print(combinarNomePokemon('Bulba'))
print(combinarNomePokemon('Char'))
print(combinarNomePokemon('Squir'))
print(combinarNomePokemon('Eevee'))
print(combinarNomePokemon('Mag'))
print(combinarNomePokemon('Mew'))


