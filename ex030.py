num = int(input('Digite um numero: '))
n = num % 2
if n == 0:
    print('\033[34mvocê digitou o numero: {}. Ele é par \033[m'.format(num))
else:
    print('\033[31mvocê digitou o numero: {}. Ele é impar\033[m'. format(num))
