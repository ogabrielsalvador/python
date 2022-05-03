
# Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.
# No final, mostre um boletim contendo a média de cada um e
# permita que o usuário possa mostrar as notas de cada aluno individualmente.

from time import sleep

boletim = []
aluno = []

while True:
    aluno.append(str(input('Nome: ')).title())
    aluno.append(float(input('Nota 1: ')))
    aluno.append(float(input('Nota 2: ')))
    aluno.append((aluno[1] + aluno[2]) / 2)
    boletim.append(aluno[:])
    aluno.clear()
    while True:
        opcao = str(input('Quer continuar? [S/N] ')).strip().upper()
        if opcao == 'S' or opcao == 'N':
            break
    if opcao == 'N':
        break
print(f'{"-=" * 25}-')

print(f'{"Nº":<4}{"NOME":<22}{"MÉDIA":>4}\n{"-" * 30}')
for i in range(0, len(boletim)):
    print(f'{i + 1:<4}{boletim[i][0]:<22}{boletim[i][3]:>4.1f}')
print('-' * 30)

while True:
    while True:
        opcao = int(input('Mostrar notas de qual aluno? [999 interrompe]: '))
        if 1 <= opcao <= len(boletim) or opcao == 999:
            break
    if opcao == 999:
        break
    print(f'As notas de {boletim[opcao - 1][0]} foram {boletim[opcao - 1][1]:.1f} e {boletim[opcao - 1][2]:.1f}\n{"-" * 51}')

print('\nFINALIZANDO...')
sleep(1)
print('\nPrograma encerrado com sucesso')
