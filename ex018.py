from math import sin, cos, tan, radians
a = float(input('Qual o angulo? A:'))

print('O seno é: {:.2f} \nO cosseno: {:.2f} \nA tangente: {:.2f} \nO angulo: {:.0f}'.format(sin(radians(a)), cos(radians(a)), tan(radians(a)), a))
