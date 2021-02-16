sexo = str(input('Digite um sexo [M/F]: ')).upper().strip()[0]
while 'F' != sexo != 'M':
    sexo = str(input('Dados invalidos. Por favor informe seu sexo: ')).upper().strip()[0]
print('O sexo que você digitou foi: {}'.format(sexo))
