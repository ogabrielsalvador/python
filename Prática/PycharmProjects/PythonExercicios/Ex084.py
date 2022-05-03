
# Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas.
# B) Uma listagem com as pessoas mais pesadas.
# C) Uma listagem com as pessoas mais leves.

grupo = []              # a lista com todos os dados. Ex: [[nome, peso], [nome, peso], [nome, peso]]
dados = []              # usado como a lista de dados de cada pessoa para adicionar na 'lista'. Ex: [nome, peso]
pesado = []
leve = []

while True:
    nome = str(input('Nome: ')).title()
    dados.append(nome)                  # adiciona nome na lista 'dados'. dados = [nome]
    peso = float(input('Peso: '))
    dados.append(peso)                  # adiciona peso na lista 'dados'. dados = [nome, peso]

    grupo.append(dados[:])              # adiciona a lista 'dados' na lista 'grupo'. grupo = [[nome, peso]]
                                        # IMPORTANTE usar o '[:]' para criar uma CÓPIA da lista 'dados.
    if len(grupo) == 1 or peso > pesado[0][1]:
        pesado.clear()
        pesado.append(dados[:])
    if peso == pesado[0][1] and nome != pesado[0][0]:
        pesado.append(dados[:])

    if len(grupo) == 1 or peso < leve[0][1]:
        leve.clear()
        leve.append(dados[:])
    if peso == leve[0][1] and nome != leve[0][0]:
        leve.append(dados[:])

    dados.clear()                    # apaga a lista 'dados' para poder preenche-la dnv na próxima repetição. dados = []

    while True:
        opcao = str(input('Quer continuar? [S/N] ')).strip().upper()
        if opcao == 'S' or opcao == 'N':
            break
    if opcao == 'N':
        break
print(f'{"-=" * 25}-')

# item A):
print(f'Ao todo, você cadastrou {len(grupo)} pessoas')

# item B):
print(f'O maior peso registrado foi de {pesado[0][1]} Kg. Peso de', end=' ')
for i in range(0, len(pesado)):
    print(pesado[i][0], end=' ')

# item C):
print(f'\nO menor peso registrado foi de {leve[0][1]} Kg. Peso de', end=' ')
for i in range(0, len(leve)):
    print(leve[i][0], end=' ')
