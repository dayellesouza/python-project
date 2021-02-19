num = int(input('Digite um numero inteiro: '))
print('''=-=-=-= Selecione uma base de conversão =-=-=-=
[ 1 ] - Converter para binário
[ 2 ] - Converter para octal
[ 3 ] - Converter para hexadecimal''')
op = int(input('Sua opção: '))

if op == 1:
    print('{} convertido para BINÁRIO é igual a {}'.format(num, bin(num)[2:]))
elif op == 2:
    print('{} convertido para OCTAL é igual a {}'.format(num, oct(num)[2:]))
elif op == 3:
    print('{} convertido para HEXADECIMAL é igual a {}'.format(num, hex(num)[2:]))
else:
    print('Opção invalida')
