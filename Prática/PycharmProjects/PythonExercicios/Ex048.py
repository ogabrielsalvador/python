
# Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de três e que se encontram no
# intervalo de 1 até 500

inicio = int(input('Qual o início do intervalo: '))
fim = int(input('Qual o final do intervalo: '))
m = int(input('Os múltiplos de qual número você quer? '))
print('''Quais os números do intervalo serão utilizados:
[ 1 ] ímpares
[ 2 ] pares
[ 0 ] ambos''')
v = int(input('Digite a sua opção: '))

if v != 0 and v != 1 and v != 2:
    print('Opção INVÁLIDA. Digite novamente!')
    exit()

s = 0
n = 0

if v == 0:
    for c in range(inicio, fim + 1):
        if c % m == 0:
            s = s + c
            n = n + 1
elif v == 2:
    for c in range(inicio, fim + 1):
        if c % 2 == 0 and c % m == 0:
            s = s + c
            n = n + 1
else:
    for c in range(inicio, fim + 1):
        if c % 2 == 1 and c % m == 0:
            s = s + c
            n = n + 1

print(f'A soma de todos os {n} valores solicitados é {s}')
