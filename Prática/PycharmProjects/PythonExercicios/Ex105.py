# Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e
# vai retornar um dicionário com as seguintes informações:
# — Quantidade de notas
# — A maior nota
# — A menor nota
# — A média da turma
# — A situação (opcional)
# Adicione também as docstrings dessa função para consulta pelo desenvolvedor.

def notas(*note, sit=False):
    """
    — > Função para analisar as notas de uma turma.

    :param note: recebe uma ou mais notas, não possui limite.
    :param sit: informa a situação das notas da turma [opcional].
    :return: retorna um dicionário dos dados da análise das notas.
    """
    dicionary = dict()
    dicionary['Quantidade de notas:'] = len(note)
    dicionary['Maior nota:'] = max(note)
    dicionary['Menor nota:'] = min(note)
    dicionary['Média:'] = sum(note) / len(note)
    if sit:
        if dicionary['Média:'] < 4:
            dicionary['Situação:'] = 'PÉSSIMA'
        elif dicionary['Média:'] < 6:
            dicionary['Situação:'] = 'RUIM'
        elif dicionary['Média:'] < 7:
            dicionary['Situação:'] = 'RAZOÁVEL'
        elif dicionary['Média:'] < 8:
            dicionary['Situação:'] = 'BOA'
        else:
            dicionary['Situação:'] = 'EXCELENTE'
    return dicionary


boletim = notas(5.5, 8.7, 9.5, 4.2)
print(boletim)

boletim = notas(5.5, 8.7, 9.5, 4.2, sit=True)
print(boletim)
