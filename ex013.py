n = float(input('Qual o valor do salário atual? R$'))

ns = n + (n * 15/100)

print('Sálario antigo: R${:.2f}. \nO valor do seu novo salário é: {:.2f} \nO aumento foi de {:.2f}'.format(n, ns, ns - n))

