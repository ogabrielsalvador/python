
# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo

n = int(input('Digite um número: '))
contador = 0

for c in range(1, n):
    if n % c == 0:
        contador += 1
if contador == 1:
    print(f'O número {n} É PRIMO')
else:
    print(f'O número {n} NÃO É PRIMO')
