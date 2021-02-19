ano = int(input('Digite o ano: '))
b = ano % 4
if b == 0:
    print('Ano bissexto')
else:
    print('Ano normal')
