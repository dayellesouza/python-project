km = float(input('Quantos KM rodado? KM:'))
dias = int(input('Quantos dias alugado? '))
pf = (km * 0.15) + (dias * 60)

print('O total a pagar é de R${:.2f}'.format(pf))
