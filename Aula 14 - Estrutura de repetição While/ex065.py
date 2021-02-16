op = 'S'
total = soma = maior = menor = 0
while op in 'Ss':
    num = int(input('Digite um numero: '))
    soma += num
    total += 1
    if total == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        elif num < menor:
            menor = num
    op = str(input('Quer continuar? [S/N] ')).lower().strip() [0]

média = soma / total

print('Você digitou {} números e a média foi {} \nO maior valor foi {} e o menor foi {}'.format(total, média, maior, menor))
