
# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados

n = int(input('Informe um número entre 0 e 9999: '))

u = n % 10
d = n // 10 % 10
c = n // 100 % 10
m = n // 1000

print(f'Analisando o número {n}')
print(f'Unidade: {u} \nDezena: {d} \nCentena: {c} \nMilhar: {m}')
