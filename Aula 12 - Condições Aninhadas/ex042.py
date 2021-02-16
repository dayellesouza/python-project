s1 = float(input('Primeiro Segmento: '))
s2 = float(input('Segundo Segmento: '))
s3 = float(input('Terceiro Segmento: '))

if s1 < s2 + s3 and s2 < s1 + s3 and s3 < s1 + s2:
    f = 'PODEM FORMAR'
else:
    f = 'NÃO PODEM FORMAR'

print('Os segmentos acima {} triângulo'.format(f))

if s1 == s3 == s2:
    print('Forma um triangulo equilátero')
elif s1 != s2 != s3 != s1:
    print('Forma um triangulo Escaleno')
else:
    print('Forma um triangulo Isóceles')
