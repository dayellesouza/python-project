l = float(input('Qual a largura da parede? '))
a = float(input('Qual a altura da parede? ' ))
ar = l * a
print('Sua parede  tem a dimensão de {:.2f}x{:.2f} e sua area é de {:.2f}m².'.format(l, a, ar))

t = ar/2
print('Você precisará de {:2}l de tinta.'.format(t))
