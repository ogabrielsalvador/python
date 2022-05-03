
# Esse arquivo é o módulo 'moeda.py' do Ex109


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
