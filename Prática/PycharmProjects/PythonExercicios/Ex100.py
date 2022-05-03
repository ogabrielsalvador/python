
# Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar().
# A primeira função vai sortear 5 números e vai colocá-los dentro da lista e
# a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.

from random import randint


def linha():
    print(f'{"-=" * 19}-')


def sorteia():
    linha()
    print('Sorteando os 5 números:')
    numeros = []
    for c in range(5):
        n = randint(1, 20)
        numeros.append(n)
        print(n, end='... ')
    print('FIM!')
    linha()
    return numeros


def somapar(numbers):
    soma = 0
    for c in numbers:
        if c % 2 == 0:
            soma += c
    print(f'O valor da soma dos números pares é {soma}')
    linha()


somapar(sorteia())
