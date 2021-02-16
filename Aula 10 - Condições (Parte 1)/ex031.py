km = float(input('Digite a distancia da viagem: '))
if km <= 200:
    km = km * 0.50
    print('O valor da viagem é R${:.2f}'.format(km))
else:
    km = km * 0.45
    print('O valor da passagem é R${:.2f}'.format(km))