nome = str(input('Digite um nome: ')).strip()
print('Seu nome em letras maiúsculas é {} '.format(nome.upper()))
print('Seu nome em letras minúsculas é {} '.format(nome.lower()))
print('Seu nome ao todo tem {} letras'.format(len(nome) - nome.count(' ')))
dividido = nome.split()
print('Seu primeiro nome é {} e tem {} letras'.format(dividido[0], len(dividido[0])))
