from math import hypot
cop = float(input('Qual o comprimento do cateto oposto? '))
cad = float(input('Qual o comprimento do cateto adjacente? '))

print('O comprimento da hipotenusa é igual a {}'.format(hypot(cop, cad)))
