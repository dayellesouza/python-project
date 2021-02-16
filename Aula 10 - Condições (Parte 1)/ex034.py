sal = float(input('Digite seu salário atual: R$'))
if sal > 1250.00:
    nsal = sal + (sal * 10/100)
    print('O valor do seu antigo salário era de {:.2f}. \nCom o aumento de 10% seu novo salário passa a ser de {:.2f}'.format(sal,nsal))
else:
    nsal = sal + (sal * 15/100)
    print('O valor do seu antigo salário era de {:.2f}. \nCom o aumento de 15% seu novo salário passa a ser de {:.2f}'.format(sal, nsal))