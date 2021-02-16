n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))

if n1 > n2:
    print('O primeiro valor é maior ( {} > {} )'.format(n1, n2))
elif n2 > n1:
    print('O segundo valor é maior ( {} > {} )'.format(n2, n1))
else:
    print('\033[31mNão existe valor maior, os dois são iguais ( {} = {} )\033[m'.format(n1, n2))
