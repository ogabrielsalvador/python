
# Desenvolva um programa que leia o primeiro termo e a razão de uma PA
# No final, mostre os 10 primeiros termos dessa progressão

print('{}\n{} 10 PRIMEIROS TERMOS DE UMA PA {}\n{}'.format('=' * 40, '\033[1;34m', '\033[m', '=' * 40))

inicio = int(input('Primeiro termo: '))
razao = int(input('Razão: '))

final = inicio + (razao * 10)       # vai ter como resultado o 11º termo da PA

for c in range(inicio, final, razao):
    print(c, end=' → ')      # a setinha ( → ) é com 'Alt + 26'
print('ACABOU')
