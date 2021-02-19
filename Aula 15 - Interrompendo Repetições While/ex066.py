# Vários números com flag
c = s = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    c += 1
    s += n
print(f'Foram digitados {c} numero, e a soma deles é {s}')
