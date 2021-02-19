cinquenta = vinte = dez = um = 0
print('-'*30)
print('{:^30}'.format('NUBANK'))
print('-'*30)
val = int(input('Qual será o valor a ser sacado? '))
total = val
ced = 50
totced = 0
while True:
    if total >= ced:
        total -= ced
        totced += 1
    else:
        if totced > 0:
            print(f'Total de {totced} cedulas de R${ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totced = 0
        if total == 0:
            break
print('=' * 30)
print('Volte sempre ao NUBANK! Tenha um bom dia!')
