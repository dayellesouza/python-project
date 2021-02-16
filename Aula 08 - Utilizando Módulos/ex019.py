from random import choice

nome1 = input('Digite o primeiro nome: ')
nome2 = input('Digite o segundo nome: ')
nome3 = input('DIgite o terceiro nome ')
nome4 = input('Digite o quarto nome: ')
arr = [nome1, nome2, nome3, nome4]
s = choice(arr)
print('O nome sorteado foi {}'.format(s))

