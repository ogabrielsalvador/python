
# Crie um programa que gerencie o aproveitamento de um jogador de futebol.
# O programa vai ler o nome do jogador e quantas partidas ele jogou.
# Depois vai ler a quantidade de gols feitos em cada partida.
# No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.

jogador = dict()
gols = []

jogador['Nome'] = str(input('Nome do jogador: ')).strip().title()
partidas = int(input(f'Quantas partidas {jogador["Nome"]} jogou? '))
s = 0
for c in range(1, partidas + 1):
    n = int(input(f'Quantos gols na partida {c}? '))
    gols.append(n)
    s += n
jogador['Gols'] = gols
jogador['Total'] = s

print('=' * 34)
print(f'O jogador {jogador["Nome"]} jogou {partidas} partidas.')
for c in range(0, len(gols)):
    print(f'   => Na partida {c + 1}, fez {gols[c]} gols')
print(f'Foi um total de {jogador["Total"]} gols.')
