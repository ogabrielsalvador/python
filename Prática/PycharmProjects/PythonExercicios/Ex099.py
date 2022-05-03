
# Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros.
# Seu programa tem que analisar todos os valores e dizer qual deles é o maior.

from random import randint


def linha():
    print('=' * 45)


def maior():
    numeros = []
    for c in range(0, randint(0, 10)):
        n = randint(0, 99)
        numeros.append(n)
        print(n, end='... ')
    print()
    linha()
    if len(numeros) == 0:
        print('Não foi informado nenhum número.')
    elif len(numeros) == 1:
        print('Foi informado apenas 1 número.')
    else:
        print(f'Foram informados {len(numeros)} números ao todo.')
    if len(numeros) != 0:
        print(f'O maior valor informado foi {max(numeros)}')
    return numeros


linha()
print('Analisando os valores')
maior()
linha()
