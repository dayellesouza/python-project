num = total = soma = 0

while num != 999:
    num = int(input('Digite um numero [ 999 para para ]: '))
    if num != 999:
        total += 1
        soma += num
print('Voce digitou {} números e a soma entre eles foi {}'.format(total, soma))
