nome = str(input('Digite seu nome completo: ')).strip()
print('Muito prazer em te conhecer!')
n = nome.split()
print('Seu primeiro nome é {}'.format(n[0]))
print('Seu último nome é {}'.format(n[len(n)-1]))

