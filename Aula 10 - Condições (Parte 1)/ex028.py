import random
c = random.randint(0, 5)
num = int(input('Qual o número que o computador gerou? '))
if c == num:
    print('Você acertou')
else:
    print('Você errou. Você digitou {} e o número é: {}'.format(num, c))
