soma = 0
cont = 0
for c in range(1, 7):
    n = int(input('Digite um numero: '))
    if n % 2 == 0:
        soma += n
        cont += 1
print('A soma de {} numeros pares é igual a {}'.format(cont, soma))
# soma somente numeros pares



