totmil = total = menor = cont = 0
barato = ''
while True:
    print('---'*10)
    print('     CADASTRO DE PRODUTO')
    print('---'*10)
    nome = str(input('Nome: '))
    preço = float(input('Preço: R$'))
    print('---' * 10)
    cont += 1
    total += preço
    if preço > 1000:
        totmil += 1
    if cont == 1 or preço < menor:
        menor = preço
        barato = nome
    quest = ' '
    while quest not in 'SN':
        quest = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if quest == 'N':
        break
print(f'O total gasto foi de R${total:.2f}')
print(f'O total de produtos que custam mais que R$1000 é {totmil}')
print(f'O nome do produto mais barato é {barato}, R${totbarato:.2f}')