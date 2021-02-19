print('Tabuada')
n = int(input('Digite um numero para saber a tabuada: '))
for c in range(0, 11):
    tab = n * c
    print('{:^} x {:^} = {:^}'.format(n, c, tab))
