'''FAÇA UM PROGRAMA QUE LEIA O ANO DE NASCIMENTO DE UM JOVEM E INFORME DE A CORDO COM SUA IDADE
SE ELE AINDA VAI SE ALISTAR
SE É HORA DE SE ALISTAR
SE  JA PASOU O TEMPO DE SE ALISTAR
O PROGRAMA DEVE MOSTRAR O TEMPO QUE FALTA E O QUE PASSOU PARA ISSO.'''

# 1 LER ANO DE NASCIMENTO
# 2 CALCULAR IDADE BASEADO NO ANO ATUAL
# 3 VERIFICAR IDADE
# 4 RETORNAR INFORMAÇAO

class Alistamento:
    def __init__(self,ano,ano_idade):
        self.ano = ano
        self.ano_idade = ano_idade


    def calc_idade(self):
        return self.ano - self.ano_idade

def user_year():
    ano = 2024
    ano_idade = int(input('Digite o seu ano de nascimento: '))


    alistamento = Alistamento(ano,ano_idade)
    idade = alistamento.calc_idade()

    if alistamento.calc_idade() > 18:
        print(f'Voce possui {idade} anos e ja passou {idade - 18} anos do periodo de alistamento.')
    elif alistamento.calc_idade() < 18:
        print(f'Voce possui {idade} anos e ainda falta {18 - idade} anos para o periodo de alsitamento.')
    else:
        print(f'Voce possui {idade} e esta no periodo de alistamento.')

def main():
    user_year()

main()