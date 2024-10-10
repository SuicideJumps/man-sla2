def pagamento_produto(preco, forma_pagamento):
    avista = preco - (preco * 0.1)
    avista_cartao = preco - (preco * 0.05)
    duas_vezes = preco
    tres_ou_mais = preco + (preco * 0.20)

    if forma_pagamento == 1:
        return f'Pagamento à vista\nValor original: R${preco:.2f}\nCom desconto de 10%: R${avista:.2f}'
    elif forma_pagamento == 2:
        return f'Pagamento à vista no cartão\nValor original: R${preco:.2f}\nCom desconto de 5%: R${avista_cartao:.2f}'
    elif forma_pagamento == 3:
        return f'Pagamento em 2x no cartão\nValor total: R${duas_vezes:.2f}'
    elif forma_pagamento == 4:
        return f'Pagamento em 3x ou mais no cartão\nValor original: R${preco:.2f}\nCom acréscimo de 20%: R${tres_ou_mais:.2f}'
    else:
        return 'Valor digitado inválido'


preco = float(input('Digite o preço do produto: '))
forma_pagamento = int(input('Forma de pagamento\n'
                            '[1] à vista\n'
                            '[2] à vista no cartão\n'
                            '[3] 2x no cartão\n'
                            '[4] 3x ou mais no cartão\n'
                            ': '))


resultado = pagamento_produto(preco, forma_pagamento)
print(resultado)
