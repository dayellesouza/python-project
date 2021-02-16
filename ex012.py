n = float(input('Digite o valor inicial: R$'))

d = n - (n * 5/100)

print('A peça custava {:.2f} \nNa promoção com 5% de desconto o Novo preço é R${:.2f} \nSeu desconto foi de {:.2f}'.format(n, d, n-d))
