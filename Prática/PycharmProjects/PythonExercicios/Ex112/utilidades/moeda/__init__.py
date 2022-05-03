
# Esse arquivo é o módulo 'moeda.py' do Ex112


def aumentar(price=0, percentage=0, sit=False):
    price = price * (1 + (percentage / 100))
    return price if sit is False else moeda(price)


def diminuir(price=0, percentage=0, sit=False):
    price = price * (1 - (percentage / 100))
    return price if sit is False else moeda(price)


def dobro(price=0, sit=False):
    price = price * 2
    return price if sit is False else moeda(price)


def metade(price, sit=False):
    price = price / 2
    return price if sit is False else moeda(price)


def moeda(price=0, unity='R$'):
    return f'{unity} {price:.2f}'.replace('.', ',')


def resumo(price=0, addition=0, reduction=0):
    print(f'{"-" * 30}\n{"RESUMO DO VALOR":^30}\n{"-" * 30}')
    print(f'Preço analisado:{moeda(price):>14}')
    print(f'Dobro do preço:{moeda(dobro(price)):>15}')
    print(f'Metade do preço:{moeda(metade(price)):>14}')
    print(f'{addition:>3}% de aumento:{aumentar(price, addition, True):>14}')
    print(f'{reduction:>3}% de desconto:{diminuir(price, reduction, True):>13}')
    print('-' * 30)
