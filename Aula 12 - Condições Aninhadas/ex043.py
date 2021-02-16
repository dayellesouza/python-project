from math import ceil

altura = float(input('Digite sua altura: (Kg) '))
peso = float(input('Digite seu peso: (m) '))

imc = peso / (altura ** 2)

if imc < 18.5:
    print('Seu IMC é {:.1f}! Você está \033[4mAbaixo do Peso\033[m'.format(imc))
elif 18.5 <= imc < 25:
    print('Seu IMC é {:.1f}! Você está no \033[4mPeso Ideal\033[m'.format(imc))
elif 25 <= imc < 30:
    print('Seu IMC é {:.1f}! Você está com \033[4mSobrepeso\033[m'.format(imc))
elif 30 <= imc < 40:
    print('Seu IMC é {:.1f}! Você está com \033[4mObesidade\033[m'.format(imc))
else:
    print('Seu IMC é {:.1f}! Você está com \033[4mObesidade Mórbida\033[m'.format(imc))

