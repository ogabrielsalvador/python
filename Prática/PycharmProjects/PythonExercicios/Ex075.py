
# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
# A) Quantas vezes apareceu o valor 9.
# B) Em que posição foi digitado o primeiro valor 3.
# C) Quais foram os números pares.

valores = tuple(int(input('Digite um valor: ')) for c in range(4))

# item A):
print(f'O valor 9 aparece {valores.count(9)} vezes')

# item B):
if 3 in valores:
    print(f'O valor 3 aparece na {valores.index(3) + 1}ª posição')
else:
    print('O valor 3 não foi digitado')

# item C):
lista = sorted(valores)
print('Os valores pares digitados foram', end=' ')
for num in lista:
    if num % 2 == 0:
        print(num, end='  ')
