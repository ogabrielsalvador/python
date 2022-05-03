
# Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais:
# o nome de um jogador e quantos gols ele marcou.
# O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.

def ficha(name='Desconhecido', goals='0'):
    """
    A função faz um print do nome do jogador e quantos gols ele fez
    :param name: nome do jogador [opcional]
    :param goals: número de gols do jogador [opcional]
    :return: não possui
    """
    if name.strip() == '':
        name = 'Desconhecido'
    if goals.strip() == '':
        goals = '0'
    print(f'O jogador {name.strip().title()} fez {goals} gol(s) no campeonato.')


ficha(str(input('Nome do jogador: ')), str(input('Número de gols: ')))
