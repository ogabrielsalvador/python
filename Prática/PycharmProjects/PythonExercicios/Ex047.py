
# Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50

for c in range(2, 51, 2):
    print('{} '.format(c), end='→ ')
print('{}ACABOU{}'.format('\033[1;31m', '\033[m'))
