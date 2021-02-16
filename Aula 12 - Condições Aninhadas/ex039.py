from datetime import date

ano = int(input('Digite o ano do seu nascimento: '))
ano_atual = date.today().year
idade = ano_atual - ano
if idade < 18:
    alistamento = 18 - idade
    print('Você ainda vai se alistar. \nFalta {} anos'.format(alistamento))
elif idade == 18:
    print('Está na hora de você se alistar :)')
else:
    alistamento = idade - 18
    print('Você passou do tempo de alistamento em {} anos'.format(alistamento))