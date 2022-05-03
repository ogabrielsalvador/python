
# Aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.

jogador = {}
gols = []
dados = []

while True:
    soma_gols = 0
    jogador['Nome'] = str(input('Nome do jogador: ')).strip().title()
    partidas = int(input(f'Quantas partidas {jogador["Nome"]} jogou? '))
    for c in range(0, partidas):
        n = int(input(f'Quantos gols na partida {c + 1}? '))
        gols.append(n)
        soma_gols += n
    jogador['Gols'] = gols[:]
    gols.clear()
    jogador['Total'] = soma_gols
    dados.append(jogador.copy())
    opcao = str(input('Quer continuar? [S/N] ')).strip().upper()
    while opcao != 'S' and opcao != 'N':
        opcao = str(input('Opção digitada INVÁLIDA! Digite novamente.\nQuer continuar? [S/N] ')).strip().upper()
    if opcao == 'N':
        break
print('=' * 40)

print(f'{"Cód.":<5}{"Nome":<22}{"Total":<8}Gols')
for c in range(0, len(dados)):
    print(f'{(c + 1):>3}  {(dados[c]["Nome"]):<22}{dados[c]["Total"]:>4}    {dados[c]["Gols"]}')
print('=' * 40)

while True:
    opcao = int(input('Mostrar dados de qual jogador? [999 para parar] '))
    while opcao < 1 or opcao > len(dados):
        print('Opção digitada INVÁLIDA! Digite novamente.')
        opcao = int(input('Mostrar dados de qual jogador? [999 para parar] '))
    print(f'  --> Dados do jogador {dados[opcao - 1]["Nome"].upper()}:')
    for i, g in enumerate(dados[opcao - 1]['Gols']):
        print(f'Na partida {i + 1:>2} foi feito {g} gol(s).')
    print('-' * 40)
    if opcao == 999:
        break
