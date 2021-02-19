#Calculo de fatorial
'''from math import factorial
num = int(input('Digite um numero para calcular seu fatorial: '))
f = factorial(num)
print('O fatorial de {} é {}'.format(num, f))'''
num = int(input('Digite um numero para calcular seu fatorial: '))
c = num
f = 1
print('Calculando fatorial de {}!'.format(num), end='')
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print('{}'.format(f))
