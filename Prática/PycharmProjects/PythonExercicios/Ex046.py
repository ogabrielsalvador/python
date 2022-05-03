
# Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício,
# indo de 10 até 0, com uma pausa de 1 segundo entre eles

from time import sleep

print(' ')
print('{}- CONTAGEM REGRESSIVA {}-'.format('-=' * 6, '-=' * 6))
print(' ')

for c in range(10, -1, -1):
    print(c)
    sleep(1)
print('{}  FELIZ ANO NOVOOO!!!  {}'.format('\033[1;30;43m', '\033[m'))
