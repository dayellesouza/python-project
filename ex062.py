pt = int(input('Digite o primeiro termo: '))  # primeiro termo
r = int(input('Digite a razão: '))  # razão
t = pt  # termo recebe primeiro termo
c = 1  # contador
total = 1
new = 10
while new != 0:
    total += new
    while c <= total:
        print('{} ► '.format(t), end='')
        t += r  # termo = termo + razão
        c += 1
    print('Pausa')
    new = int(input('Quantos termos voce quer mostrar? '))
print('Finalizamos com {} termos mostrado'.format(total))