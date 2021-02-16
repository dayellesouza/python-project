# Menu de opções
from time import sleep

maior = 0
op = 0
n1 = int(input('Digite o 1º valor: '))
n2 = int(input('Digite o 2º valor: '))

while op != 5:
    sleep(0.5)
    print('-=-'*10)
    print('Escolha uma das opções abaixo')
    print('''\033[33m    [ 1 ] Somar
    [ 2 ] Multiplicar
    [ 3 ] Maior
    [ 4 ] Novos Números
    [ 5 ] Sair do Programa \033[m''')
    op = int(input('-----> Qual sua opção? '))

    if op == 1:
        soma = n1 + n2
        print('A soma entre {} + {} é igual a {}'.format(n1, n2, soma))
        sleep(0.5)
    elif op == 2:
        multi = n1 * n2
        print('A multiplicação entre {} * {} é igual a {}'.format(n1, n2, multi))
        sleep(0.5)
    elif op == 3:
        maior = n1
        if n2 > n1:
            maior = n2
        print('Entre {} e {} o maior é {}'.format(n1, n2, maior))
        sleep(0.5)
    elif op == 4:
        print('Digite novos números')
        n1 = int(input('1º valor: '))
        n2 = int(input('2º valor: '))
        sleep(0.5)
    elif op == 5:
        print('Finalizando...')
        sleep(1)
    else:
        print('Opção invalida. Tente novamente')
sleep(1)
print('Fim do programa. Volte sempre')