cont_homem = cont18 = cont_mulher = 0
while True:
    print('---'*10)
    print('     CADASTRE UMA PESSOA')
    print('---' * 10)
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).upper().strip()[0]
    print('---'*10)
    if idade >= 18:
        cont18 += 1
    if sexo == 'M':
        cont_homem += 1
    if sexo == 'F' and idade <= 20:
        cont_mulher += 1
    quest = ' '
    while quest not in 'SN':
        quest = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if quest == 'N':
        break
print(f'O total de pessoas com mais de 18 anos é {cont18}')
print(f'O total de homens cadastrados foi de {cont_homem}')
print(f'O total de mulhers com menos de 20 anos foi de {cont_mulher}')
