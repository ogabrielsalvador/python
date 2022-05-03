
# Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira

from math import trunc

n = float(input('Insira um número real qualquer: '))

print('A parte inteira de {} é {}.'.format(n, int(n)))

# Com o uso da importação de Ex107 (math)

print('A parte inteira de {} é {}.'.format(n, trunc(n)))
