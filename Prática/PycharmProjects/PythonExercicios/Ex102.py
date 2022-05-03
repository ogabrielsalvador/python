
# Crie um programa que tenha uma função fatorial() que receba dois parâmetros:
# o primeiro que indique o número a calcular
# e outro chamado show, que será um valor lógico (opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial.


def fatorial(number=1, show=False):
    """
    A função retorna o valor fatorial de um número
    :param number: número que terá seu fatorial calculado
    :param show: determina se será feito o print ou não do cálculo + resultado
    :return: valor fatorial do 'number'
    """
    f = 1
    for c in range(number, 0, -1):
        f *= c
        if show is True:
            if c != 1:
                print(f'{c} x ', end='')
            else:
                print(f'{c} = {f}')
    return f


fatorial(int(input('Digite um número: ')), show=True)
