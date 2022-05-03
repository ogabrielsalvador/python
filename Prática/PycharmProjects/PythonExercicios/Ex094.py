
# Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário
# e todos os dicionários em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas
# B) A média de idade
# C) Uma lista com as mulheres
# D) Uma lista de pessoas com idade acima da média

dados = dict()
lista = []
soma_idade = 0

while True:
    dados['Nome'] = str(input('Nome: ')).strip().title()
    dados['Sexo'] = str(input('Sexo: [M/F] ')).strip().upper()
    while dados['Sexo'] != 'M' and dados['Sexo'] != 'F':
        print(f'Digite um sexo válido!', end=' ')
        dados['Sexo'] = str(input('Sexo: [M/F] ')).strip().upper()
    dados['Idade'] = int(input('Idade: '))
    soma_idade += dados['Idade']
    lista.append(dados.copy())
    while True:
        opcao = str(input('Quer continuar? [S/N] ')).strip().upper()
        if opcao in 'SN':
            break
    if opcao == 'N':
        break
print('=' * 25)

# A)
print(f'Ao todo foram cadastradas {len(lista)} pessoas.')

# B)
print(f'A média de idade é de {soma_idade / len(lista):.2f} anos.')

# C)
print('As mulheres cadastradas foram:')
for c in range(0, len(lista)):
    if lista[c]['Sexo'] == 'F':
        print(f'  --> A {lista[c]["Nome"]} com {lista[c]["Idade"]} anos de idade.')

# D)
print('As pessoas com idade acima da média são:')
for c in range(0, len(lista)):
    if lista[c]['Idade'] >= (soma_idade / len(lista)):
        print(f'  --> {lista[c]["Nome"]} com {lista[c]["Idade"]} anos de idade.')
