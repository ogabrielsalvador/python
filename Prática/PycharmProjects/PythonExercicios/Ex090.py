
# Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário.
# No final, mostre o conteúdo da estrutura na tela.

boletim = dict()

boletim['Nome'] = str(input('Digite o nome? ')).title()
boletim['Média'] = float(input(f'Qual a média de {boletim["Nome"]}? '))
if boletim['Média'] >= 6:
    boletim['Situação'] = 'APROVADO'
else:
    boletim['Situação'] = 'REPROVADO'

print(f'\n{boletim}\n')

for k, v in boletim.items():
    print(f'{k:>8} --> {v}')
