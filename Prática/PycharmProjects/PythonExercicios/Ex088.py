
# Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
# O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo,
# cadastrando tudo em uma lista composta.

from random import randint

print(f'{"-" * 35}\n{"JOGO NA MEGA SENA":^35}\n{"-" * 35}')

lista = []
jogos = []

a = int(input('Quantos jogos você quer que eu sorteie? '))

for c in range(a):
    while len(jogos) < 6:
        n = randint(1, 60)
        if n not in jogos:
            jogos.append(n)
    lista.append(sorted(jogos[:]))
    jogos.clear()

for i in range(0, a):
    print(f'Jogo {i + 1:>2}: ', end='')
    for j in range(0, 5):
        print(f'{lista[i][j]:>2}', end=', ')
    print(f'{lista[i][5]:>2}.')
