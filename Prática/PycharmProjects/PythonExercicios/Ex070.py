
# Crie um programa que leia o nome e o preço de vários produtos.
# O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
# A) qual é o total gasto na compra.
# B) quantos produtos custam mais de R$1000.
# C) qual é o nome do produto mais barato.

titulo = 'LOJA DO BARATÃO'
print('{}\n{}{}{}\n{}'.format('-' * 45, '\033[1;32m', titulo.center(45), '\033[m', '-' * 45))

nome = str(input('Nome do Produto: ')).capitalize()
preco = float(input('Preço: R$ '))

total = preco                # item A
caro = 0                     # item B
if preco > 1000:
    caro += 1
barato = preco               # item C
nomebarato = nome

while True:
    while True:
        opcao = str(input('Quer continuar? [S/N] ')).upper()
        if opcao in 'SN':
            break
    if opcao == 'N':
        break
    nome = str(input('Nome do Produto: ')).capitalize()
    preco = float(input('Preço: R$ '))
    total += preco
    if preco > 1000:
        caro += 1
    if preco < barato:
        barato = preco
        nomebarato = nome
print('{} FIM DO PROGRAMA {}'.format('-' * 14, '-' * 14))

print(f'O total da compra foi de R$ {total:.2f}\nTemos {caro} produtos custando mais de R$ 1000.00\n'
      f'O produto mais barato foi {nomebarato} que custou R$ {barato:.2f}')
