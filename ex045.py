from random import randint
itens = ('Pedra', 'Papel', 'Tesoura')
comp = randint(0, 2)
print('''[ 0 ] pedra
[ 1 ] papel
[ 2 ] tesoura''')
joken = int(input('Selecione uma opção: '))
win = '\033[34mVocê venceu\033[m'
won = '\033[31mVocê perdeu\033[m'
draw = '\033[33mEmpate\033[m'
print('O computador escolheu: {}'.format(itens[comp]))
print('O jogador escolheu: {}'.format(itens[joken]))

if comp == 0:
    if joken == 0:
        print(draw)
    elif 1 == joken:
        print(win)
    elif joken == 2:
        print(won)
    else:
        print('Jogada invalida')
elif comp == 1:
    if joken == 0:
        print(won)
    elif joken == 1:
        print(draw)
    elif joken == 2:
        print(win)
    else:
        print('Jogada invalida')
elif comp == 2:
    if joken == 0:
        print(win)
    elif joken == 1:
        print(won)
    elif joken == 2:
        print(draw)
    else:
        print('Jogada invalida')
