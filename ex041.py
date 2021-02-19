from datetime import date
atual = date.today().year
nasc = int(input('Digite o ano de nascimento do aluno: '))
idade = atual - nasc

if idade <= 9:
    print('Idade: {} \nCategoria: Mirim'.format(idade))
elif idade <= 14:
    print('Idade: {} \nCategoria: Infantil'.format(idade))
elif idade <= 19:
    print('Idade: {} \nCategoria: Junior'.format(idade))
elif idade <= 25:
    print('Idade: {} \nCategoria: Sênior'.format(idade))
else:
    print('Idade: {} \nCategoria: Master'.format(idade))
