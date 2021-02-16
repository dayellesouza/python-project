val = float(input('Qual o preço do produto? '))
print('''[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
op = int(input('Qual a forma de pagamento? '))

if 1 == op == 2:
    desc = val - val * (10 / 100)
    print('O valor original do produto era {:.2f}!'
          '\nO produto teve 10% de desconto. \nValor final: {:.2f}'.format(val, desc))
elif op == 2:
    desc = val - val * (5 / 100)
    print('O valor original do produto era {:.2f}!'
          '\nConsiderando a forma de pagamento, o produto teve 5% de desconto. \nValor final: {:.2f}'.format(val, desc))
elif op == 3:
    div = val / 2
    print('O valor do produto é {:.2f}! \nPrestações: 2x de {:.2f}'.format(val, div))
elif op == 4:
    parc = int(input('Quantas parcelas? '))
    juros = val + val * (20 / 100)
    div = juros / parc
    print('O valor do produto é {:.2f}! (Possui 20% de Juros) '
          '\nPrestações: {}x de {:.2f}'.format(juros, parc, div))
else:
    print('Opção invalida. Tente novamente')
