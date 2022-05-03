
# Escreva um programa que leia um número N inteiro qualquer e
# mostre na tela os N primeiros elementos de uma Sequência de Fibonacci

print('{}\n{} Sequência de Fibonacci {}\n{}'.format('-' * 24, '\033[1;34m', '\033[m', '-' * 24))
n = int(input('Quantos termos você quer mostrar? '))

c = 0
a1 = 1
a2 = 1
a3 = a1 + a2

print(a1, end=' → ')
while c < (n - 1):
    print(a2, end=' → ')
    a1 = a2
    a2 = a3
    a3 = a1 + a2
    c += 1
