def imc_calc(peso,altura):
    return  peso / (altura * altura)

peso = float(input('Diga seu peso: '))
altura = float(input('Diga sua altura: '))

imc = imc_calc(peso,altura)

print(f'Seu IMC é: {imc:.2f} ')

if 0 < imc < 18.5:
    print('Abaixo do peso')
elif 18.5 <= imc < 25:
    print('Peso ideal')
elif 25 <= imc < 30:
    print('Sobrepeso')
elif 30 <= imc < 40:
    print('Oseso')
else:
    print('morbius')


