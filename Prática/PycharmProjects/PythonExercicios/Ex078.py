
# Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
# No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.

numeros = []
for c in range(0, 5):
    numeros.append(int(input(f'Digite um valor para a posição {c}: ')))

print(f'Você digitou os valores:', end=' ')     # print da lista dos valores digitados
for num in numeros:
    print(num, end='  ')
print('')

pos_maior = []      # lista das posições do MAIOR numero
pos_menor = []      # lista das posições do MENOR numero
p = 0               # contador das posições
for num in numeros:
    if num == max(numeros):
        pos_maior.append(p)
    if num == min(numeros):
        pos_menor.append(p)
    p += 1

print(f'O maior valor digitado foi {max(numeros)} nas posições', end=' ')
for p in pos_maior:
    print(p, end='... ')
print('')

print(f'O menor valor digitado foi {min(numeros)} nas posições', end=' ')
for p in pos_menor:
    print(p, end='... ')
print('')
