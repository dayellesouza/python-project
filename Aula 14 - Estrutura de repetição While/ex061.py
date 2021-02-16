"""pt = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))
dec = pt + (10 - 1) * r

for c in range(pt, dec + r, r):
    print(c, end=' ')
print('\nAcabou')"""
pt = int(input('Digite o primeiro termo: '))  # primeiro termo
r = int(input('Digite a razão: '))  # razão
t = pt  # termo recebe primeiro termo
c = 1  # contador
while c <= 10:
    print('{} ► '.format(t), end='')
    t += r  # termo = termo + razão
    c += 1
print('Fim')
