print('Mostrando a soma de todos numeros impares que são multiplos de 3')
soma = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        soma += c  # acumulador
        cont += 1  # contador
print('total de numeros: {}. A soma é: {}'.format(cont, soma))
