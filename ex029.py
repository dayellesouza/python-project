km = float(input('Digite a velocidade do carro: '))

if km >= 80:
    multa = (km - 80) * 7.00
    print('Você está multado. O valor da multa é: {}'.format(multa))
else:
    print('Você está OK!')
