
# Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
# Guarde esses resultados em um dicionário em Python.
# No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.

from random import randint
from time import sleep
from operator import itemgetter

jogo = {}
rank = []

print('Valores sorteados:')
for c in range(0, 4):
    jogo['Jogador 0' + str(c + 1)] = randint(1, 6)
    print(f'O Jogador 0{c + 1} tirou o número {jogo["Jogador 0" + str(c + 1)]} no dado')
    sleep(.5)

print(f'{"=" * 37}\n{"RANKING DE JOGADORES":^37}\n{"=" * 37}')

rank = sorted(jogo.items(), key=itemgetter(1), reverse=True)

for i, v in enumerate(rank):
    print(f'   {i + 1}º lugar: {v[0]} com {v[1]}.')
    sleep(.5)
