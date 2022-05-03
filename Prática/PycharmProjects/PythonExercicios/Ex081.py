
# Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
# A) Quantos números foram digitados.
# B) A lista de valores, ordenada de forma decrescente.
# C) Se o valor 5 foi digitado e está ou não na lista.

lista = []

while True:
    lista.append(int(input('Digite um valor: ')))
    while True:
        opcao = str(input('Quer continuar? [S/N] ')).upper()
        if opcao in 'SN':
            break
    if opcao == 'N':
        break

# item A):
print(f'\nVocê digitou {len(lista)} elementos.')

# item B):
print(f'Os valores digitados em ordem decrescente são:', end=' ')
for n in sorted(lista)[::-1]:
    print(n, end=' ')
print('')

# item C):
print('O valor 5 está na lista' if 5 in lista else 'O valor 5 não está na lista')
