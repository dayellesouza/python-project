
pt = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))
dec = pt + (10 - 1) * r

for c in range(pt, dec + r, r):
    print(c, end=' ')
print('\nAcabou')


