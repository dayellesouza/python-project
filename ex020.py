from random import shuffle
a1 = str(input('Digite o primeiro nome: '))
a2 = str(input('Digite o segundo nome: '))
a3 = str(input('Digite o terceiro nome: '))
a4 = str(input('Digite o quarto nome: '))
arr = [a1, a2, a3, a4]
shuffle(arr)
print('A ordem sorteada foi {}')
print(arr)