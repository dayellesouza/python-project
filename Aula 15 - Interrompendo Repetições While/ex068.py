# Esse programa simula um jogo de par ou impar
from random import randint
v = 0
while True:
    jogador = int(input('Diga um valor: '))
    pc = randint(0, 10)
    total = jogador + pc
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Impar? [P/I] ')).strip().upper()[0]
    print(f'Você jogou {jogador} e o computador jogou {pc}. Total de {total}', end=' ')
    print('DEU PAR' if total % 2 == 0 else 'DEU IMPAR')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você GANHOU!')
            print('-' * 26)
            v += 1
        else:
            print('Você PERDEU!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Você GANHOU!')
            print('-' * 26)
            v += 1
        else:
            print('Você PERDEU!')
            break
    print('Vamos jogar novamente')
print(f'GAME OVER! Venceu {v} vezes')
