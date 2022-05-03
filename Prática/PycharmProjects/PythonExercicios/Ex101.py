
# Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa,
# retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.


def voto(age=0, born=0):
    """
    Essa função retorna o direito eleitoral do usuário (voto negado, opcional ou obrigatório)
    O dev pode declarar apenas um ou nenhum parâmetro

    :param age: idade do usuário
    :param born: ano de nascimento do usuário
    :return: situação do direito eleitoral do usuário (voto negado, opcional ou obrigatório)

    dev: Gabriel LINDÃO S2
    """
    from datetime import datetime
    if age == 0 and born == 0:
        born = int(input('Em que ano você nasceu? '))
    if age == 0:
        age = datetime.today().year - born
    if age < 16:
        return 'VOTO NEGADO'
    elif age < 18 or age >= 65:
        return 'VOTO OPCIONAL'
    else:
        return 'VOTO OBRIGATÓRIO'


# declarando/usando a variavel idade (age)
idade = int(input('Digite a sua idade? '))
print(f'O seu direito eleitoral é de {voto(age=idade)}')

# sem declarar variavel, especificando o parâmetro nascimento (born)
nascimento = int(input('Em que ano você nasceu? '))
print(f'O seu direito eleitoral é de {voto(born=nascimento)}')

# sem especificar nenhum parâmetro
print(f'O seu direito eleitoral é de {voto()}')

# imprimir o help da função
print()
help(voto)
