from math import ceil

val_casa = float(input('Qual o valor da casa? R$'))
sal = float(input('Qual o seu salário atual? R$'))
anos = int(input('Quantos anos de financiamento? '))

val_prest = val_casa / (anos * 12)
teto = sal * (30 / 100)

if val_prest <= teto:
    print(
        '\033[34mParabéns, seu emprestimo foi aprovado! \nO valor da casa é R${:.2f} \nem {} anos. \nA prestação ficou estipulada em R${:.2f}\033[m'.format(
            val_casa, anos, ceil(teto)))
else:
    print(
        '\033[31mInfelizmente seu emprestimo não foi aprovado! \nO valor de prestações ( R${:.2f} ) excedeu os 30% do seu salário\033[m'.format(
            ceil(teto)))
