nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
média = (nota1 + nota2) / 2

if média >=7:
    print('A média das notas foi {:.1f}! \033[34mAPROVADO\033[m'.format(média))
elif média >= 5.0 and média <= 6.9:
    print('A média das notas foi {:.1f}! \033[33mRECUPERAÇÃO\033[m'.format(média))
else:
    print('A média das notas foi {:.1f}! \033[31mREPROVADO\033[m'.format(média))