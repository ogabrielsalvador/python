
# Faça um programa que leia um número qualquer e mostre o seu fatorial

print('Digite um número para')
n = int(input('calcular seu Fatorial: '))
print(f'Calculando {n}! =', end=' ')
f = 1

while n > 0:
    f = f * n
    if (n - 1) == 0:
        print(n, end=' ')
    else:
        print(f'{n} x', end=' ')
    n = n - 1

print('={} {}{}'.format('\033[1;31m', f, '\033[m'))
