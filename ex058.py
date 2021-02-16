#Jogo de adivinhar o numero que o computador pensou
from random import randint
pc = randint(0, 10)
print('Acabei de pensar em um numero de 0 a 10. Consegue adivinhar?')
num = int(input('Qual o seu palpite: '))
cont = 0
while num != pc:
    num = int(input('\nErrado. Tente outra vez: '))
    cont += 1
    if num < pc:
        print('\nMais. Tente mais uma vez')
    elif num > pc:
        print('Menos.Tente de novo')
print('Voce acertou. O computador pensou em: {} e voce em {}. Seu numero de tentativas foi {}'.format(pc, num, cont))