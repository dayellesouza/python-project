somaidade = 0
maioridadehomem = 0
totmulher20 = 0
nomevelho = ''
for dados in range(1, 5):
    print('----- {}ª PESSOA -----'.format(dados))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    somaidade += idade
    if dados == 1 and sexo in 'Mm':
        maioridadehomem += idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher20 += 1

mediaidade = somaidade / 4
print('A média de idades do grupo é {} anos'.format(mediaidade))
print('O homem mais velho do grupo se chama {} e tem {} anos'.format(nome, maioridadehomem))
print('Ao todo são {} mulheres de menos de 20 anos'.format(totmulher20))
