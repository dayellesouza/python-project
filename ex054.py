from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0
for pess in range(1, 8):
    ano = int(input('Em que ano a {}ª pessoa nasceu? '.format(pess)))
    idade = atual - ano
    if idade >= 21:
        totmaior += 1
    else:
        totmenor += 1
print('ao todo, tivemos {} pessoas maiores de idade'.format(totmaior))
print('e também tivemos {} pessoas menores de idade'.format(totmenor))
