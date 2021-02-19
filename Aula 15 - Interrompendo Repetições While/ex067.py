# Tabuada v3.0
while True:
    print('--*' * 16)
    n = int(input('Digite um número para saber a Tabuada: '))
    if n < 0:
        break
    for c in range (1, 11):
        print(f'{n} x {c} = {n*c}')
print('Encerrando... Volte Sempre!')