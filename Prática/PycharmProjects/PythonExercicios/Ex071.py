
# Crie um programa que simule o funcionamento de um caixa eletrônico.
# No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas
# cédulas de cada valor serão entregues.
# OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.

titulo = 'CAIXA ELETRÔNICO'
print('{}\n{}{}{}\n{}'.format('=' * 30, '\033[1;31m', titulo.center(30), '\033[m', '=' * 30))

saque = int(input('Qual o valor que você quer sacar? R$ '))

total = saque
n50 = n20 = n10 = n1 = 0
while True:
    if total < 50 and n50 != 0:
        print(f'Total de {n50} cédulas de R$ 50')
        break
    if total < 50:
        break
    total -= 50
    n50 += 1
while True:
    if total < 20 and n20 != 0:
        print(f'Total de {n20} cédulas de R$ 20')
        break
    if total < 20:
        break
    total -= 20
    n20 += 1
while True:
    if total < 10 and n10 != 0:
        print(f'Total de {n10} cédulas de R$ 10')
        break
    if total < 10:
        break
    total -= 10
    n10 += 1
while True:
    if total == 0 and n1 != 0:
        print(f'Total de {n1} cédulas de R$ 1')
        break
    if total == 0:
        break
    total -= 1
    n1 += 1
print('=' * 30)
